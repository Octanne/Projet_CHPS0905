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
renderView1.CenterOfRotation = [76.25, 95.75, 63.25]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-268.3438377809511, -51.88340348214558, 293.48912308613797]
renderView1.CameraFocalPoint = [76.25000000000001, 95.75000000000003, 63.25000000000001]
renderView1.CameraViewUp = [-0.6109489134579686, 0.5712573367440257, -0.5480934960028724]
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

absolutePath='/home/corentin/Documents/Cours/M2/S9/CHPS0905 - Imagerie Médicale/'

# create a new 'DICOM Reader (directory)'
ax_3DTOF = DICOMReaderdirectory(registrationName='Ax_3DTOF', FileName=absolutePath+'Projet2025/DICOM/Ax_3DTOF')

# create a new 'DICOM Reader (directory)'
sag_GRE2 = DICOMReaderdirectory(registrationName='Sag_GRE2', FileName=absolutePath+'Projet2025/DICOM/Sag_GRE2')

# create a new 'DICOM Reader (directory)'
sag_Optm = DICOMReaderdirectory(registrationName='Sag_Optm', FileName=absolutePath+'Projet2025/DICOM/Sag_Optm')

# create a new 'DICOM Reader (directory)'
sag_GRE = DICOMReaderdirectory(registrationName='Sag_GRE', FileName=absolutePath+'Projet2025/DICOM/Sag_GRE')

# create a new 'DICOM Reader (directory)'
sag_PCA = DICOMReaderdirectory(registrationName='Sag_PCA', FileName=absolutePath+'Projet2025/DICOM/Sag_PCA')

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from ax_3DTOF
ax_3DTOFDisplay = Show(ax_3DTOF, renderView1, 'UniformGridRepresentation')

# get 2D transfer function for 'DICOMImage'
dICOMImageTF2D = GetTransferFunction2D('DICOMImage')
dICOMImageTF2D.ScalarRangeInitialized = 1
dICOMImageTF2D.Range = [0.0, 182.0, 0.0, 1.0]

# get color transfer function/color map for 'DICOMImage'
dICOMImageLUT = GetColorTransferFunction('DICOMImage')
dICOMImageLUT.TransferFunction2D = dICOMImageTF2D
dICOMImageLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 404.5, 0.865003, 0.865003, 0.865003, 809.0, 0.705882, 0.0156863, 0.14902]
dICOMImageLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'DICOMImage'
dICOMImagePWF = GetOpacityTransferFunction('DICOMImage')
dICOMImagePWF.Points = [0.0, 0.0, 0.5, 0.0, 425.1501770019531, 0.0, 0.5, 0.0, 573.3453979492188, 0.486607164144516, 0.5, 0.0, 777.41748046875, 0.9508929252624512, 0.5, 0.0, 809.0, 1.0, 0.5, 0.0]
dICOMImagePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
ax_3DTOFDisplay.Representation = 'Volume'
ax_3DTOFDisplay.ColorArrayName = ['POINTS', 'DICOMImage']
ax_3DTOFDisplay.LookupTable = dICOMImageLUT
ax_3DTOFDisplay.SelectNormalArray = 'None'
ax_3DTOFDisplay.SelectTangentArray = 'None'
ax_3DTOFDisplay.SelectTCoordArray = 'None'
ax_3DTOFDisplay.TextureTransform = 'Transform2'
ax_3DTOFDisplay.OSPRayScaleArray = 'DICOMImage'
ax_3DTOFDisplay.OSPRayScaleFunction = 'Piecewise Function'
ax_3DTOFDisplay.Assembly = ''
ax_3DTOFDisplay.SelectedBlockSelectors = ['']
ax_3DTOFDisplay.SelectOrientationVectors = 'None'
ax_3DTOFDisplay.ScaleFactor = 19.150000000000002
ax_3DTOFDisplay.SelectScaleArray = 'DICOMImage'
ax_3DTOFDisplay.GlyphType = 'Arrow'
ax_3DTOFDisplay.GlyphTableIndexArray = 'DICOMImage'
ax_3DTOFDisplay.GaussianRadius = 0.9575
ax_3DTOFDisplay.SetScaleArray = ['POINTS', 'DICOMImage']
ax_3DTOFDisplay.ScaleTransferFunction = 'Piecewise Function'
ax_3DTOFDisplay.OpacityArray = ['POINTS', 'DICOMImage']
ax_3DTOFDisplay.OpacityTransferFunction = 'Piecewise Function'
ax_3DTOFDisplay.DataAxesGrid = 'Grid Axes Representation'
ax_3DTOFDisplay.PolarAxes = 'Polar Axes Representation'
ax_3DTOFDisplay.ScalarOpacityUnitDistance = 0.8912560001413409
ax_3DTOFDisplay.ScalarOpacityFunction = dICOMImagePWF
ax_3DTOFDisplay.TransferFunction2D = dICOMImageTF2D
ax_3DTOFDisplay.OpacityArrayName = ['POINTS', 'DICOMImage']
ax_3DTOFDisplay.ColorArray2Name = ['POINTS', 'DICOMImage']
ax_3DTOFDisplay.IsosurfaceValues = [381.0]
ax_3DTOFDisplay.SliceFunction = 'Plane'
ax_3DTOFDisplay.Slice = 126
ax_3DTOFDisplay.SelectInputVectors = [None, '']
ax_3DTOFDisplay.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
ax_3DTOFDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 762.0, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
ax_3DTOFDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 762.0, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
ax_3DTOFDisplay.SliceFunction.Origin = [76.25, 95.75, 63.25]

# show data from sag_GRE
sag_GREDisplay = Show(sag_GRE, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
sag_GREDisplay.Representation = 'Volume'
sag_GREDisplay.ColorArrayName = ['POINTS', 'DICOMImage']
sag_GREDisplay.LookupTable = dICOMImageLUT
sag_GREDisplay.SelectNormalArray = 'None'
sag_GREDisplay.SelectTangentArray = 'None'
sag_GREDisplay.SelectTCoordArray = 'None'
sag_GREDisplay.TextureTransform = 'Transform2'
sag_GREDisplay.OSPRayScaleArray = 'DICOMImage'
sag_GREDisplay.OSPRayScaleFunction = 'Piecewise Function'
sag_GREDisplay.Assembly = ''
sag_GREDisplay.SelectedBlockSelectors = ['']
sag_GREDisplay.SelectOrientationVectors = 'None'
sag_GREDisplay.ScaleFactor = 12.700000000000001
sag_GREDisplay.SelectScaleArray = 'DICOMImage'
sag_GREDisplay.GlyphType = 'Arrow'
sag_GREDisplay.GlyphTableIndexArray = 'DICOMImage'
sag_GREDisplay.GaussianRadius = 0.635
sag_GREDisplay.SetScaleArray = ['POINTS', 'DICOMImage']
sag_GREDisplay.ScaleTransferFunction = 'Piecewise Function'
sag_GREDisplay.OpacityArray = ['POINTS', 'DICOMImage']
sag_GREDisplay.OpacityTransferFunction = 'Piecewise Function'
sag_GREDisplay.DataAxesGrid = 'Grid Axes Representation'
sag_GREDisplay.PolarAxes = 'Polar Axes Representation'
sag_GREDisplay.ScalarOpacityUnitDistance = 1.732050807568877
sag_GREDisplay.ScalarOpacityFunction = dICOMImagePWF
sag_GREDisplay.TransferFunction2D = dICOMImageTF2D
sag_GREDisplay.OpacityArrayName = ['POINTS', 'DICOMImage']
sag_GREDisplay.ColorArray2Name = ['POINTS', 'DICOMImage']
sag_GREDisplay.IsosurfaceValues = [404.5]
sag_GREDisplay.SliceFunction = 'Plane'
sag_GREDisplay.Slice = 63
sag_GREDisplay.SelectInputVectors = [None, '']
sag_GREDisplay.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
sag_GREDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 809.0, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
sag_GREDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 809.0, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
sag_GREDisplay.SliceFunction.Origin = [63.5, 63.5, 63.5]

# show data from sag_GRE2
sag_GRE2Display = Show(sag_GRE2, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
sag_GRE2Display.Representation = 'Volume'
sag_GRE2Display.ColorArrayName = ['POINTS', 'DICOMImage']
sag_GRE2Display.LookupTable = dICOMImageLUT
sag_GRE2Display.SelectNormalArray = 'None'
sag_GRE2Display.SelectTangentArray = 'None'
sag_GRE2Display.SelectTCoordArray = 'None'
sag_GRE2Display.TextureTransform = 'Transform2'
sag_GRE2Display.OSPRayScaleArray = 'DICOMImage'
sag_GRE2Display.OSPRayScaleFunction = 'Piecewise Function'
sag_GRE2Display.Assembly = ''
sag_GRE2Display.SelectedBlockSelectors = ['']
sag_GRE2Display.SelectOrientationVectors = 'None'
sag_GRE2Display.ScaleFactor = 12.700000000000001
sag_GRE2Display.SelectScaleArray = 'DICOMImage'
sag_GRE2Display.GlyphType = 'Arrow'
sag_GRE2Display.GlyphTableIndexArray = 'DICOMImage'
sag_GRE2Display.GaussianRadius = 0.635
sag_GRE2Display.SetScaleArray = ['POINTS', 'DICOMImage']
sag_GRE2Display.ScaleTransferFunction = 'Piecewise Function'
sag_GRE2Display.OpacityArray = ['POINTS', 'DICOMImage']
sag_GRE2Display.OpacityTransferFunction = 'Piecewise Function'
sag_GRE2Display.DataAxesGrid = 'Grid Axes Representation'
sag_GRE2Display.PolarAxes = 'Polar Axes Representation'
sag_GRE2Display.ScalarOpacityUnitDistance = 1.732050807568877
sag_GRE2Display.ScalarOpacityFunction = dICOMImagePWF
sag_GRE2Display.TransferFunction2D = dICOMImageTF2D
sag_GRE2Display.OpacityArrayName = ['POINTS', 'DICOMImage']
sag_GRE2Display.ColorArray2Name = ['POINTS', 'DICOMImage']
sag_GRE2Display.IsosurfaceValues = [241.0]
sag_GRE2Display.SliceFunction = 'Plane'
sag_GRE2Display.Slice = 63
sag_GRE2Display.SelectInputVectors = [None, '']
sag_GRE2Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
sag_GRE2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 482.0, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
sag_GRE2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 482.0, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
sag_GRE2Display.SliceFunction.Origin = [63.5, 63.5, 63.5]

# show data from sag_Optm
sag_OptmDisplay = Show(sag_Optm, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
sag_OptmDisplay.Representation = 'Volume'
sag_OptmDisplay.ColorArrayName = ['POINTS', 'DICOMImage']
sag_OptmDisplay.LookupTable = dICOMImageLUT
sag_OptmDisplay.SelectNormalArray = 'None'
sag_OptmDisplay.SelectTangentArray = 'None'
sag_OptmDisplay.SelectTCoordArray = 'None'
sag_OptmDisplay.TextureTransform = 'Transform2'
sag_OptmDisplay.OSPRayScaleArray = 'DICOMImage'
sag_OptmDisplay.OSPRayScaleFunction = 'Piecewise Function'
sag_OptmDisplay.Assembly = ''
sag_OptmDisplay.SelectedBlockSelectors = ['']
sag_OptmDisplay.SelectOrientationVectors = 'None'
sag_OptmDisplay.ScaleFactor = 12.700000000000001
sag_OptmDisplay.SelectScaleArray = 'DICOMImage'
sag_OptmDisplay.GlyphType = 'Arrow'
sag_OptmDisplay.GlyphTableIndexArray = 'DICOMImage'
sag_OptmDisplay.GaussianRadius = 0.635
sag_OptmDisplay.SetScaleArray = ['POINTS', 'DICOMImage']
sag_OptmDisplay.ScaleTransferFunction = 'Piecewise Function'
sag_OptmDisplay.OpacityArray = ['POINTS', 'DICOMImage']
sag_OptmDisplay.OpacityTransferFunction = 'Piecewise Function'
sag_OptmDisplay.DataAxesGrid = 'Grid Axes Representation'
sag_OptmDisplay.PolarAxes = 'Polar Axes Representation'
sag_OptmDisplay.ScalarOpacityUnitDistance = 1.732050807568877
sag_OptmDisplay.ScalarOpacityFunction = dICOMImagePWF
sag_OptmDisplay.TransferFunction2D = dICOMImageTF2D
sag_OptmDisplay.OpacityArrayName = ['POINTS', 'DICOMImage']
sag_OptmDisplay.ColorArray2Name = ['POINTS', 'DICOMImage']
sag_OptmDisplay.IsosurfaceValues = [259.5]
sag_OptmDisplay.SliceFunction = 'Plane'
sag_OptmDisplay.Slice = 63
sag_OptmDisplay.SelectInputVectors = [None, '']
sag_OptmDisplay.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
sag_OptmDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 519.0, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
sag_OptmDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 519.0, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
sag_OptmDisplay.SliceFunction.Origin = [63.5, 63.5, 63.5]

# show data from sag_PCA
sag_PCADisplay = Show(sag_PCA, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
sag_PCADisplay.Representation = 'Volume'
sag_PCADisplay.ColorArrayName = ['POINTS', 'DICOMImage']
sag_PCADisplay.LookupTable = dICOMImageLUT
sag_PCADisplay.SelectNormalArray = 'None'
sag_PCADisplay.SelectTangentArray = 'None'
sag_PCADisplay.SelectTCoordArray = 'None'
sag_PCADisplay.TextureTransform = 'Transform2'
sag_PCADisplay.OSPRayScaleArray = 'DICOMImage'
sag_PCADisplay.OSPRayScaleFunction = 'Piecewise Function'
sag_PCADisplay.Assembly = ''
sag_PCADisplay.SelectedBlockSelectors = ['']
sag_PCADisplay.SelectOrientationVectors = 'None'
sag_PCADisplay.ScaleFactor = 12.700000000000001
sag_PCADisplay.SelectScaleArray = 'DICOMImage'
sag_PCADisplay.GlyphType = 'Arrow'
sag_PCADisplay.GlyphTableIndexArray = 'DICOMImage'
sag_PCADisplay.GaussianRadius = 0.635
sag_PCADisplay.SetScaleArray = ['POINTS', 'DICOMImage']
sag_PCADisplay.ScaleTransferFunction = 'Piecewise Function'
sag_PCADisplay.OpacityArray = ['POINTS', 'DICOMImage']
sag_PCADisplay.OpacityTransferFunction = 'Piecewise Function'
sag_PCADisplay.DataAxesGrid = 'Grid Axes Representation'
sag_PCADisplay.PolarAxes = 'Polar Axes Representation'
sag_PCADisplay.ScalarOpacityUnitDistance = 1.732050807568877
sag_PCADisplay.ScalarOpacityFunction = dICOMImagePWF
sag_PCADisplay.TransferFunction2D = dICOMImageTF2D
sag_PCADisplay.OpacityArrayName = ['POINTS', 'DICOMImage']
sag_PCADisplay.ColorArray2Name = ['POINTS', 'DICOMImage']
sag_PCADisplay.IsosurfaceValues = [91.0]
sag_PCADisplay.SliceFunction = 'Plane'
sag_PCADisplay.Slice = 63
sag_PCADisplay.SelectInputVectors = [None, '']
sag_PCADisplay.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
sag_PCADisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 182.0, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
sag_PCADisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 182.0, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
sag_PCADisplay.SliceFunction.Origin = [63.5, 63.5, 63.5]

# setup the color legend parameters for each legend in this view

# get color legend/bar for dICOMImageLUT in view renderView1
dICOMImageLUTColorBar = GetScalarBar(dICOMImageLUT, renderView1)
dICOMImageLUTColorBar.Title = 'DICOMImage'
dICOMImageLUTColorBar.ComponentTitle = ''

# set color bar visibility
dICOMImageLUTColorBar.Visibility = 1

# show color legend
ax_3DTOFDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
sag_GREDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
sag_GRE2Display.SetScalarBarVisibility(renderView1, True)

# show color legend
sag_OptmDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
sag_PCADisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.ViewModules = renderView1
animationScene1.Cues = timeAnimationCue1
animationScene1.AnimationTime = 0.0

# initialize the animation scene

# ----------------------------------------------------------------
# restore active source
SetActiveSource(sag_PCA)
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
