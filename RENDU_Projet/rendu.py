import os
import numpy as np
import SimpleITK as sitk
import pyvista as pv
import matplotlib.pyplot as plt

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

# Register Sag_Flux mask (from segmentation) to Stokes mask (we assume similar masks exist)
fixed_img = binary['Sag_Optm']  # use optimized as fixed
moving_img = binary['Sag_GRE']  # example
transform = elastix_rigid(fixed_img, moving_img)

# -----------------------------
# 6. FLOW COMPARISON
# -----------------------------
# Read vector volumes
sag_flux = pv.read('Projet2025/VTK_Files/Sag_Flux.vtk')       # STRUCTURED_POINTS with vectors & scalars
stokes = pv.read('Projet2025/VTK_Files/Stokes.vtu')            # UNSTRUCTURED_GRID with Velocity & Pressure

# Apply the computed transform to Stokes points
transform_filter = pv.transform.Transform()
transform_filter.SetTransform(sitk.TransformParameterMapToSITK(transform))
transformed_stokes = stokes.transform(transform_filter)

# Extract velocity vectors and their norms
vf_sag = np.array(sag_flux['vectors'])
norm_sag = np.linalg.norm(vf_sag, axis=1)

vf_stokes = np.array(transformed_stokes['Velocity'])
norm_stokes = np.linalg.norm(vf_stokes, axis=1)

# Scatter plot of norms
plt.figure()
plt.scatter(norm_stokes, norm_sag, s=2)
plt.xlabel('Stokes Velocity Norm')
plt.ylabel('Sag Flux Velocity Norm')
plt.title('Velocity Norm Comparison')
plt.show()

# Save transform for future use
sitk.WriteParameterObject(transform, 'rigid_transform.txt')
# Save transformed Stokes for visualization
transformed_stokes.save('transformed_stokes.vtu')
# Save filtered images for visualization
for name, img in filtered.items():
    sitk.WriteImage(img, f'filtered_{name}.nii.gz')
# Save binary masks for visualization
for name, mask in binary.items():
    sitk.WriteImage(mask, f'binary_{name}.nii.gz')
# Save surfaces for visualization
for name, surface in surfaces.items():
    surface.save(f'surface_{name}.vtk')
# Save filtered images for visualization
for name, img in filtered.items():
    sitk.WriteImage(img, f'filtered_{name}.nii.gz')
# Save binary masks for visualization
for name, mask in binary.items():
    sitk.WriteImage(mask, f'binary_{name}.nii.gz')
# Save surfaces for visualization
for name, surface in surfaces.items():
    surface.save(f'surface_{name}.vtk')
# Save transformed Stokes for visualization
transformed_stokes.save('transformed_stokes.vtu')