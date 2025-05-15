import os
import numpy as np
import SimpleITK as sitk
import pyvista as pv
import matplotlib.pyplot as plt
from vtkmodules.vtkCommonTransforms import vtkTransform
from sklearn.decomposition import PCA

# -----------------------------
# 1. READ DICOM VOLUMES
# -----------------------------
def read_dicom_series(directory):
    reader = sitk.ImageSeriesReader()
    series_ids = reader.GetGDCMSeriesIDs(directory)
    if not series_ids:
        raise ValueError(f"No DICOM series found in {directory}")
    # Use first series
    series_file_names = reader.GetGDCMSeriesFileNames(directory, series_ids[0])
    reader.SetFileNames(series_file_names)
    image = reader.Execute()
    return image

# Example directories
dicom_dirs = {
    'Ax_3DTOF': 'Projet2025/DICOM/Ax_3DTOF',
    'Sag_GRE': 'Projet2025/DICOM/Sag_GRE',
    'Sag_Optm': 'Projet2025/DICOM/Sag_Optm'
}

volumes = {name: read_dicom_series(dir) for name, dir in dicom_dirs.items()}

# -----------------------------
# 2. FILTERING
# -----------------------------
def filter_image(img, time_step=0.125, n_iter=5):
    smoother = sitk.CurvatureFlowImageFilter()
    smoother.SetTimeStep(time_step)
    smoother.SetNumberOfIterations(n_iter)
    return smoother.Execute(img)

filtered = {name: filter_image(img) for name, img in volumes.items()}

# -----------------------------
# 3. SEGMENTATION & BINARIZATION
# -----------------------------
def segment_and_binarize(img, lower_thresh, upper_thresh):
    thresh = sitk.BinaryThreshold(img, lowerThreshold=lower_thresh,
                                  upperThreshold=upper_thresh, insideValue=1, outsideValue=0)
    # Keep largest connected component
    cc = sitk.ConnectedComponent(thresh)
    stats = sitk.LabelShapeStatisticsImageFilter()
    stats.Execute(cc)
    largest_label = max(stats.GetLabels(), key=lambda l: stats.GetPhysicalSize(l))
    largest_cc = sitk.BinaryThreshold(cc, lowerThreshold=largest_label,
                                      upperThreshold=largest_label, insideValue=1, outsideValue=0)
    return largest_cc

# Example threshold values - adjust per dataset
binary = {name: segment_and_binarize(img, 150, 4096)
          for name, img in filtered.items() if name in ['Sag_GRE', 'Sag_Optm']}

# -----------------------------
# 4. SURFACE REPRESENTATION
# -----------------------------
def mask_to_surface(mask, spacing):
    arr = sitk.GetArrayFromImage(mask)
    grid = pv.wrap(arr)
    grid.spacing = spacing[::-1]  # flip z,y,x to x,y,z
    surface = grid.contour(isosurfaces=[0.5])
    return surface

surfaces = {name: mask_to_surface(mask, volumes[name].GetSpacing())
            for name, mask in binary.items()}

# -----------------------------
# 5. REGISTRATION
# -----------------------------
def elastix_rigid(fixed, moving):
    elastix = sitk.ElastixImageFilter()
    elastix.SetFixedImage(fixed)
    elastix.SetMovingImage(moving)
    elastix.SetParameterMap(sitk.GetDefaultParameterMap('rigid'))
    elastix.Execute()
    transform = elastix.GetTransformParameterMap()[0]
    return transform

# Helper: Convert SimpleITK parameter map to vtkTransform
def sitk_parameter_map_to_vtk_transform(param_map):
    """
    Convert a SimpleITK Elastix parameter map (rigid) to a vtkTransform,
    taking into account the center of rotation.
    """
    transform = vtkTransform()
    params = param_map['TransformParameters']
    params = [float(x) for x in params]
    # For rigid: [angleX, angleY, angleZ, transX, transY, transZ]
    if param_map['Transform'][0] == 'EulerTransform':
        angles = params[:3]
        translation = params[3:6]
        # Get center of rotation if present
        center = [0.0, 0.0, 0.0]
        if 'CenterOfRotationPoint' in param_map:
            center = [float(x) for x in param_map['CenterOfRotationPoint']]
        # Apply: T(center) * R * T(-center) * T(translation)
        transform.PostMultiply()
        transform.Translate(center)
        transform.RotateZ(np.degrees(angles[2]))
        transform.RotateY(np.degrees(angles[1]))
        transform.RotateX(np.degrees(angles[0]))
        transform.Translate([-c for c in center])
        transform.Translate(translation)
    else:
        # fallback: just translation
        translation = params[-3:]
        transform.Translate(translation)
    return transform

# -----------------------------
# 6. FLOW COMPARISON
# -----------------------------
# Read vector volumes
sag_flux = pv.read('Projet2025/VTK_Files/Sag_Flux.vtk')        # STRUCTURED_POINTS with vectors & scalars
stokes = pv.read('Projet2025/VTK_Files/Stokes.vtu')            # UNSTRUCTURED_GRID with Velocity & Pressure

# Register Sag_Flux mask (from segmentation) to Stokes mask
fixed_img = binary['Sag_Optm']  # use optimized as fixed
moving_img = binary['Sag_GRE']  # use GRE as moving
transform = elastix_rigid(fixed_img, moving_img)

# Display the transform parameters
print("Transform parameters:")
for key, value in transform.items():
    if isinstance(value, list):
        val_str = ' '.join(str(v) for v in value)
        print(f'({key} {val_str})')
    else:
        print(f'({key} {value})')

# Apply the computed transform to Stokes points
vtk_rigid_transform = sitk_parameter_map_to_vtk_transform(transform)
transformed_stokes = stokes.transform(vtk_rigid_transform)

# Test: translation manuelle pour voir l'effet
manual_transform = vtkTransform()
manual_transform.Translate(30, 0, 0)  # décale de 30 mm sur X
test_stokes = stokes.transform(manual_transform)
test_stokes.save('test_stokes_translated.vtu')

# Extract velocity vectors and their norms
vf_sag = np.array(sag_flux['vectors'])
norm_sag = np.linalg.norm(vf_sag, axis=1)

vf_stokes = np.array(transformed_stokes['Velocity'])
norm_stokes = np.linalg.norm(vf_stokes, axis=1)

# Ensure both arrays are the same length for scatter plot
min_len = min(len(norm_stokes), len(norm_sag))
norm_stokes = norm_stokes[:min_len]
norm_sag = norm_sag[:min_len]

# Scatter plot of norms
plt.figure()
plt.scatter(norm_stokes, norm_sag, s=2)
plt.xlabel('Stokes Velocity Norm')
plt.ylabel('Sag Flux Velocity Norm')
plt.title('Velocity Norm Comparison')
plt.savefig('velocity_norm_comparison.png')
plt.close()

# Visualisation et sauvegarde des surfaces
plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(surfaces['Sag_GRE'], color='red', opacity=0.5, label='Sag_GRE')
plotter.add_mesh(surfaces['Sag_Optm'], color='blue', opacity=0.5, label='Sag_Optm')
plotter.add_legend()
plotter.show(screenshot='results/surface_overlap.png')
# Nom de la figure : Superposition des surfaces Sag_GRE et Sag_Optm

# Visualiser Stokes transformé et Sag Flux
# plotter = pv.Plotter(off_screen=True)
# plotter.add_mesh(sag_flux.glyph(orient='vectors', scale=False, factor=1.0), color='green', label='Sag_Flux')
# plotter.add_mesh(transformed_stokes.glyph(orient='Velocity', scale=False, factor=1.0), color='orange', label='Stokes (transformed)')
# plotter.add_legend()
# plotter.show(screenshot='results/vector_comparison.png')

stokes_vtu = pv.read('Projet2025/VTK_Files/Stokes.vtu')
# Save as VTK for consistent handling
os.makedirs('results', exist_ok=True)
stokes_vtu.save('results/Stokes.vtk')
stokes_vtk = pv.read('results/Stokes.vtk')

def apply_transform(mesh, param_map):
    # Extract parameters from the ParameterMap dictionary
    params = [float(x) for x in param_map['TransformParameters']]
    if 'CenterOfRotationPoint' in param_map:
        center = np.array([float(x) for x in param_map['CenterOfRotationPoint']])
    else:
        center = np.array([0.0, 0.0, 0.0])
    t = np.array(params[3:6])
    euler = sitk.Euler3DTransform()
    euler.SetCenter(center)
    euler.SetParameters(params)
    R = np.array(euler.GetMatrix()).reshape(3, 3)
    pts = mesh.points
    shifted = pts - center
    rotated = shifted @ R.T
    trans_pts = rotated + center + t
    m2 = mesh.copy()
    m2.points = trans_pts
    return m2

stokes_reg = apply_transform(stokes_vtk, transform)
stokes_reg.save('results/Stokes_registered.vtk')

# Visualiser Stokes transformé et Sag Flux
p = pv.Plotter(off_screen=True)
sag_glyph = sag_flux.glyph(orient='vectors', scale='vectors', factor=0.2)
stokes_glyph = stokes_reg.glyph(orient='Velocity', scale='Velocity', factor=0.2)
p.add_mesh(sag_glyph, color='green', opacity=0.1)
p.add_mesh(stokes_glyph, color='orange', opacity=0.5)
p.show(screenshot='results/vector_comparison.png')
# Nom de la figure : Superposition des vecteurs Sag_Flux et Stokes transformé

# Save transform for future use
with open('rigid_transform.txt', 'w') as f:
    for key, value in transform.items():
        if isinstance(value, list):
            val_str = ' '.join(str(v) for v in value)
            f.write(f'({key} {val_str})\n')
        else:
            f.write(f'({key} {value})\n')

# Save transformed Stokes for visualization
transformed_stokes.save('transformed_stokes.vtu')
# Save surfaces for visualization
for name, surface in surfaces.items():
    surface.save(f'surface_{name}.vtk')
# Save surfaces for visualization
for name, surface in surfaces.items():
    surface.save(f'surface_{name}.vtk')
# Save transformed Stokes for visualization
transformed_stokes.save('transformed_stokes.vtu')

# Additional geometry information for debugging
print("Sag_GRE origin:", volumes['Sag_GRE'].GetOrigin())
print("Sag_GRE spacing:", volumes['Sag_GRE'].GetSpacing())
print("Sag_Optm direction:", volumes['Sag_Optm'].GetDirection())
print("Sag_Optm origin:", volumes['Sag_Optm'].GetOrigin())
print("Sag_Optm spacing:", volumes['Sag_Optm'].GetSpacing())
print("Sag_GRE direction:", volumes['Sag_GRE'].GetDirection())
print("Stokes bounds:", stokes.bounds)
print("Sag_Flux bounds:", sag_flux.bounds)

def compute_main_orientation(points):
    # PCA sur XY uniquement (pour rotation Z)
    pca = PCA(n_components=2)
    pca.fit(points[:, :2])
    # direction du 1er axe principal
    direction = pca.components_[0]
    angle_rad = np.arctan2(direction[1], direction[0])
    return np.degrees(angle_rad)

def compute_main_orientation_xz(points):
    # PCA sur XZ uniquement (rotation autour de Y)
    xz = points[:, [0, 2]]
    pca = PCA(n_components=2)
    pca.fit(xz)
    direction = pca.components_[0]
    angle_rad = np.arctan2(direction[1], direction[0])
    return np.degrees(angle_rad)

def compute_main_orientation_yz(points):
    # PCA sur YZ uniquement (rotation autour de X)
    yz = points[:, [1, 2]]
    pca = PCA(n_components=2)
    pca.fit(yz)
    direction = pca.components_[0]
    angle_rad = np.arctan2(direction[1], direction[0])
    return np.degrees(angle_rad)

# Calcul orientation de chaque surface (Sag_Optm et Stokes)
optm_points = surfaces['Sag_Optm'].points
stokes_points = stokes.points

angle_optm = compute_main_orientation(optm_points)
angle_stokes = compute_main_orientation(stokes_points)

# Différence angulaire entre les deux
angle_to_align = angle_optm - angle_stokes

print(f"Angle Optm : {angle_optm:.2f}°")
print(f"Angle Stokes : {angle_stokes:.2f}°")
print(f"⇒ Rotation nécessaire sur Z : {angle_to_align:.2f}°")

angle_optm_xz = compute_main_orientation_xz(optm_points)
angle_stokes_xz = compute_main_orientation_xz(stokes_points)
angle_y_to_align = angle_optm_xz - angle_stokes_xz
# angle_y_to_align = 25 - 145

print(f"Angle Optm (XZ): {angle_optm_xz:.2f}°")
print(f"Angle Stokes (XZ): {angle_stokes_xz:.2f}°")
print(f"⇒ Rotation nécessaire sur Y : {angle_y_to_align:.2f}°")

angle_optm_yz = compute_main_orientation_yz(optm_points)
angle_stokes_yz = compute_main_orientation_yz(stokes_points)
angle_x_to_align = angle_optm_yz - angle_stokes_yz

print(f"Angle Optm (YZ): {angle_optm_yz:.2f}°")
print(f"Angle Stokes (YZ): {angle_stokes_yz:.2f}°")
print(f"⇒ Rotation nécessaire sur X : {angle_x_to_align:.2f}°")

# Calcul centre du Stokes
stokes_center = np.mean(stokes.points, axis=0)

align_transform = vtkTransform()
align_transform.PostMultiply()

# Translate vers origine (centre à 0)
align_transform.Translate(-stokes_center)

# Rotation autour de l'axe spécifié
align_transform.RotateY(angle_y_to_align)
align_transform.RotateZ(angle_to_align)
align_transform.RotateX(angle_x_to_align)

# Translate retour (ramène le modèle à sa position d'origine)
align_transform.Translate(stokes_center)

# Appliquer le décalage pour aligner les centres
optm_center = np.mean(surfaces['Sag_Optm'].points, axis=0)
shift = optm_center - stokes_center
align_transform.Translate(shift)

# Transformer le modèle
stokes_aligned = stokes.transform(align_transform)
stokes_aligned.save('stokes_aligned_to_optm.vtu')

# Logs
print("Décalage appliqué à Stokes pour alignement visuel :", shift)
print("Rotation appliquée :", angle_to_align, "° sur Z, ", angle_y_to_align, "° sur Y", angle_x_to_align, "° sur X")
print("Centre de rotation :", stokes_center)

