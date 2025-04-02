# state file generated using paraview version 5.13.2
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1174, 776]
renderView1.AxesGrid = 'Grid Axes 3D Actor'
renderView1.CenterOfRotation = [1.420074462890625, 23.33269500732422, 57.26286315917969]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-13.435902527766354, -100.62831431817204, 992.0209572669544]
renderView1.CameraFocalPoint = [1.4200744628906212, 23.332695007324247, 57.26286315917968]
renderView1.CameraViewUp = [0.14776124178563263, -0.9807428602386161, -0.12771083555026239]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 137.777674171108
renderView1.LegendGrid = 'Legend Grid Actor'
renderView1.PolarGrid = 'Polar Grid Actor'
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1174, 776)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

absolutePath='/home/corentin/Documents/Cours/M2/CHPS0905/'

# create a new 'Legacy VTK Reader'
sag_GREvtk = LegacyVTKReader(registrationName='Sag_GRE.vtk', FileNames=[absolutePath+'Projet2025/VTK_Files/Sag_GRE.vtk'])
UpdatePipeline()
Hide(sag_GREvtk)

# create a new 'Legacy VTK Reader'
ax_3DTOFvtk = LegacyVTKReader(registrationName='Ax_3DTOF.vtk', FileNames=[absolutePath+'Projet2025/VTK_Files/Ax_3DTOF.vtk'])
UpdatePipeline()
Hide(ax_3DTOFvtk)

# create a new 'XML Unstructured Grid Reader'
stokesvtu = XMLUnstructuredGridReader(registrationName='Stokes.vtu', FileName=[absolutePath+'Projet2025/VTK_Files/Stokes.vtu'])
stokesvtu.CellArrayStatus = ['Label']
stokesvtu.PointArrayStatus = ['Velocity', 'Pressure']
stokesvtu.TimeArray = 'None'
UpdatePipeline()
Hide(stokesvtu)

# create a new 'Legacy VTK Reader'
sag_Fluxvtk = LegacyVTKReader(registrationName='Sag_Flux.vtk', FileNames=[absolutePath+'Projet2025/VTK_Files/Sag_Flux.vtk'])
UpdatePipeline()
Hide(sag_Fluxvtk)

# ----------------------------------------------------------------
# We tranform to center all the vtk files in 0 0 0 (center on the center of the image)
# ----------------------------------------------------------------
# Center all the VTK files at (0, 0, 0)

# Function to compute the center of a dataset
def compute_center(dataset):
    bounds = dataset.GetDataInformation().GetBounds()
    center = [(bounds[0] + bounds[1]) / 2.0, (bounds[3] + bounds[2]) / 2.0, (bounds[5] + bounds[4]) / 2.0]
    print('Center:', center)
    return center

# Function to apply a translation to center the dataset at (0, 0, 0)
def center_dataset(dataset):
    center = compute_center(dataset)
    transform = Transform(Input=dataset)
    transform.Transform.Translate = [-center[0], -center[1], -center[2]]
    UpdatePipeline()
    return transform

# Center each dataset
sag_GREvtk_centered = center_dataset(sag_GREvtk)
ax_3DTOFvtk_centered = center_dataset(ax_3DTOFvtk)
stokesvtu_centered = center_dataset(stokesvtu)
sag_Fluxvtk_centered = center_dataset(sag_Fluxvtk)

# ----------------------------------------------------------------
# We do a resample to image to have a better performance
# ----------------------------------------------------------------
# Function to resample a dataset to an image
def resample_to_image(dataset, sampling_dimensions=(350, 350, 350)):
    resample = ResampleToImage(Input=dataset)
    resample.SamplingDimensions = sampling_dimensions
    return resample

# Resample each centered dataset
sag_GREvtk_resampled = resample_to_image(sag_GREvtk_centered, sampling_dimensions=(350, 350, 350))
ax_3DTOFvtk_resampled = resample_to_image(ax_3DTOFvtk_centered, sampling_dimensions=(350, 350, 350))
stokesvtu_resampled = resample_to_image(stokesvtu_centered, sampling_dimensions=(350, 350, 350))
sag_Fluxvtk_resampled = resample_to_image(sag_Fluxvtk_centered, sampling_dimensions=(350, 350, 350))

# ----------------------------------------------------------------
# We do the colorization of the datasets
# ----------------------------------------------------------------



##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------