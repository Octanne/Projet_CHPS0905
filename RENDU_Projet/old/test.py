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
renderView1.ViewSize = [1174, 497]
renderView1.AxesGrid = 'Grid Axes 3D Actor'
renderView1.CenterOfRotation = [1.420074462890625, 23.33269500732422, 57.26286315917969]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-3.3134976335286526, -16.16510275825977, 355.1055990461144]
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
layout1.SetSize(1174, 497)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Legacy VTK Reader'
sag_Fluxvtk = LegacyVTKReader(registrationName='Sag_Flux.vtk', FileNames=['/home/corentin/Documents/Cours/M2/S9/CHPS0905 - Imagerie Médicale/Projet2025/VTK_Files/Sag_Flux.vtk'])

# create a new 'XML Unstructured Grid Reader'
stokesvtu = XMLUnstructuredGridReader(registrationName='Stokes.vtu', FileName=['/home/corentin/Documents/Cours/M2/S9/CHPS0905 - Imagerie Médicale/Projet2025/VTK_Files/Stokes.vtu'])
stokesvtu.CellArrayStatus = ['Label']
stokesvtu.PointArrayStatus = ['Velocity', 'Pressure']
stokesvtu.TimeArray = 'None'

# create a new 'Legacy VTK Reader'
ax_3DTOFvtk = LegacyVTKReader(registrationName='Ax_3DTOF.vtk', FileNames=['/home/corentin/Documents/Cours/M2/S9/CHPS0905 - Imagerie Médicale/Projet2025/VTK_Files/Ax_3DTOF.vtk'])

# create a new 'Transform'
transform2 = Transform(registrationName='Transform2', Input=ax_3DTOFvtk)
transform2.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform2.Transform.Translate = [-1.4200733900070048, -23.332691192626996, -57.26286315917986]

# create a new 'Resample To Image'
resampleToImage2 = ResampleToImage(registrationName='ResampleToImage2', Input=transform2)
resampleToImage2.SamplingDimensions = [200, 200, 200]
resampleToImage2.SamplingBounds = [-76.25, 76.25, -95.75, 95.75, -63.250000000000156, 63.250000000000156]

# create a new 'Transform'
transform3 = Transform(registrationName='Transform3', Input=stokesvtu)
transform3.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform3.Transform.Translate = [34.39373314380646, -120.83572387695312, -181.6728515625]

# create a new 'Resample To Image'
resampleToImage3 = ResampleToImage(registrationName='ResampleToImage3', Input=transform3)
resampleToImage3.SamplingDimensions = [200, 200, 200]
resampleToImage3.SamplingBounds = [-30.453418731689453, 30.453418731689453, -71.47843933105469, 71.47843933105469, -20.005020141601562, 20.005020141601562]

# create a new 'Transform'
transform4 = Transform(registrationName='Transform4', Input=sag_Fluxvtk)
transform4.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform4.Transform.Translate = [-129.2754, -26.714699999999997, -175.078]

# create a new 'Legacy VTK Reader'
sag_GREvtk = LegacyVTKReader(registrationName='Sag_GRE.vtk', FileNames=['/home/corentin/Documents/Cours/M2/S9/CHPS0905 - Imagerie Médicale/Projet2025/VTK_Files/Sag_GRE.vtk'])

# create a new 'Transform'
transform1 = Transform(registrationName='Transform1', Input=sag_GREvtk)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Translate = [-129.275400400162, -26.714653015137003, -175.07763290405]

# create a new 'Resample To Image'
resampleToImage1 = ResampleToImage(registrationName='ResampleToImage1', Input=transform1)
resampleToImage1.SamplingDimensions = [200, 200, 200]
resampleToImage1.SamplingBounds = [-63.5, 63.5, -63.5, 63.5, -63.5, 63.5]

# create a new 'Resample To Image'
resampleToImage4 = ResampleToImage(registrationName='ResampleToImage4', Input=transform4)
resampleToImage4.SamplingDimensions = [200, 200, 200]
resampleToImage4.SamplingBounds = [-63.499999999999986, 63.5, -63.5, 63.5, -63.5, 63.5]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from resampleToImage1
resampleToImage1Display = Show(resampleToImage1, renderView1, 'UniformGridRepresentation')

# get 2D transfer function for 'scalars'
scalarsTF2D = GetTransferFunction2D('scalars')
scalarsTF2D.ScalarRangeInitialized = 1
scalarsTF2D.Range = [0.0, 163.0, 0.0, 1.0]

# get color transfer function/color map for 'scalars'
scalarsLUT = GetColorTransferFunction('scalars')
scalarsLUT.TransferFunction2D = scalarsTF2D
scalarsLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 81.5, 0.865003, 0.865003, 0.865003, 163.0, 0.705882, 0.0156863, 0.14902]
scalarsLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'scalars'
scalarsPWF = GetOpacityTransferFunction('scalars')
scalarsPWF.Points = [0.0, 0.0, 0.5, 0.0, 92.0240249633789, 0.0, 0.5, 0.0, 93.98197937011719, 0.3482142984867096, 0.5, 0.0, 163.0, 1.0, 0.5, 0.0]
scalarsPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
resampleToImage1Display.Representation = 'Volume'
resampleToImage1Display.ColorArrayName = ['POINTS', 'scalars']
resampleToImage1Display.LookupTable = scalarsLUT
resampleToImage1Display.SelectNormalArray = 'None'
resampleToImage1Display.SelectTangentArray = 'None'
resampleToImage1Display.SelectTCoordArray = 'None'
resampleToImage1Display.TextureTransform = 'Transform2'
resampleToImage1Display.OSPRayScaleArray = 'scalars'
resampleToImage1Display.OSPRayScaleFunction = 'Piecewise Function'
resampleToImage1Display.Assembly = ''
resampleToImage1Display.SelectedBlockSelectors = ['']
resampleToImage1Display.SelectOrientationVectors = 'None'
resampleToImage1Display.ScaleFactor = 12.699987300000002
resampleToImage1Display.SelectScaleArray = 'scalars'
resampleToImage1Display.GlyphType = 'Arrow'
resampleToImage1Display.GlyphTableIndexArray = 'scalars'
resampleToImage1Display.GaussianRadius = 0.6349993650000001
resampleToImage1Display.SetScaleArray = ['POINTS', 'scalars']
resampleToImage1Display.ScaleTransferFunction = 'Piecewise Function'
resampleToImage1Display.OpacityArray = ['POINTS', 'scalars']
resampleToImage1Display.OpacityTransferFunction = 'Piecewise Function'
resampleToImage1Display.DataAxesGrid = 'Grid Axes Representation'
resampleToImage1Display.PolarAxes = 'Polar Axes Representation'
resampleToImage1Display.ScalarOpacityUnitDistance = 1.1053780532200748
resampleToImage1Display.ScalarOpacityFunction = scalarsPWF
resampleToImage1Display.TransferFunction2D = scalarsTF2D
resampleToImage1Display.OpacityArrayName = ['POINTS', 'scalars']
resampleToImage1Display.ColorArray2Name = ['POINTS', 'scalars']
resampleToImage1Display.IsosurfaceValues = [81.5]
resampleToImage1Display.SliceFunction = 'Plane'
resampleToImage1Display.Slice = 99
resampleToImage1Display.SelectInputVectors = [None, '']
resampleToImage1Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
resampleToImage1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 163.0, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
resampleToImage1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 163.0, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
resampleToImage1Display.SliceFunction.Origin = [7.105427357601002e-15, 7.105427357601002e-15, 7.105427357601002e-15]

# show data from resampleToImage2
resampleToImage2Display = Show(resampleToImage2, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
resampleToImage2Display.Representation = 'Outline'
resampleToImage2Display.ColorArrayName = ['POINTS', '']
resampleToImage2Display.SelectNormalArray = 'None'
resampleToImage2Display.SelectTangentArray = 'None'
resampleToImage2Display.SelectTCoordArray = 'None'
resampleToImage2Display.TextureTransform = 'Transform2'
resampleToImage2Display.OSPRayScaleArray = 'scalars'
resampleToImage2Display.OSPRayScaleFunction = 'Piecewise Function'
resampleToImage2Display.Assembly = ''
resampleToImage2Display.SelectedBlockSelectors = ['']
resampleToImage2Display.SelectOrientationVectors = 'None'
resampleToImage2Display.ScaleFactor = 19.149980850000002
resampleToImage2Display.SelectScaleArray = 'scalars'
resampleToImage2Display.GlyphType = 'Arrow'
resampleToImage2Display.GlyphTableIndexArray = 'scalars'
resampleToImage2Display.GaussianRadius = 0.9574990425000001
resampleToImage2Display.SetScaleArray = ['POINTS', 'scalars']
resampleToImage2Display.ScaleTransferFunction = 'Piecewise Function'
resampleToImage2Display.OpacityArray = ['POINTS', 'scalars']
resampleToImage2Display.OpacityTransferFunction = 'Piecewise Function'
resampleToImage2Display.DataAxesGrid = 'Grid Axes Representation'
resampleToImage2Display.PolarAxes = 'Polar Axes Representation'
resampleToImage2Display.ScalarOpacityUnitDistance = 1.3846988582254665
resampleToImage2Display.OpacityArrayName = ['POINTS', 'scalars']
resampleToImage2Display.ColorArray2Name = ['POINTS', 'scalars']
resampleToImage2Display.IsosurfaceValues = [359.0]
resampleToImage2Display.SliceFunction = 'Plane'
resampleToImage2Display.Slice = 99
resampleToImage2Display.SelectInputVectors = [None, '']
resampleToImage2Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
resampleToImage2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 718.0, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
resampleToImage2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 718.0, 1.0, 0.5, 0.0]

# show data from resampleToImage3
resampleToImage3Display = Show(resampleToImage3, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
resampleToImage3Display.Representation = 'Outline'
resampleToImage3Display.ColorArrayName = [None, '']
resampleToImage3Display.SelectNormalArray = 'None'
resampleToImage3Display.SelectTangentArray = 'None'
resampleToImage3Display.SelectTCoordArray = 'None'
resampleToImage3Display.TextureTransform = 'Transform2'
resampleToImage3Display.OSPRayScaleArray = 'Label'
resampleToImage3Display.OSPRayScaleFunction = 'Piecewise Function'
resampleToImage3Display.Assembly = ''
resampleToImage3Display.SelectedBlockSelectors = ['']
resampleToImage3Display.SelectOrientationVectors = 'None'
resampleToImage3Display.ScaleFactor = 14.295673570523071
resampleToImage3Display.SelectScaleArray = 'Label'
resampleToImage3Display.GlyphType = 'Arrow'
resampleToImage3Display.GlyphTableIndexArray = 'Label'
resampleToImage3Display.GaussianRadius = 0.7147836785261535
resampleToImage3Display.SetScaleArray = ['POINTS', 'Label']
resampleToImage3Display.ScaleTransferFunction = 'Piecewise Function'
resampleToImage3Display.OpacityArray = ['POINTS', 'Label']
resampleToImage3Display.OpacityTransferFunction = 'Piecewise Function'
resampleToImage3Display.DataAxesGrid = 'Grid Axes Representation'
resampleToImage3Display.PolarAxes = 'Polar Axes Representation'
resampleToImage3Display.ScalarOpacityUnitDistance = 0.8063262128085248
resampleToImage3Display.OpacityArrayName = ['POINTS', 'Label']
resampleToImage3Display.ColorArray2Name = ['POINTS', 'Label']
resampleToImage3Display.SliceFunction = 'Plane'
resampleToImage3Display.Slice = 99
resampleToImage3Display.SelectInputVectors = ['POINTS', 'Velocity']
resampleToImage3Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
resampleToImage3Display.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 6.0, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
resampleToImage3Display.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 6.0, 1.0, 0.5, 0.0]

# show data from resampleToImage4
resampleToImage4Display = Show(resampleToImage4, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
resampleToImage4Display.Representation = 'Outline'
resampleToImage4Display.ColorArrayName = ['POINTS', '']
resampleToImage4Display.SelectNormalArray = 'None'
resampleToImage4Display.SelectTangentArray = 'None'
resampleToImage4Display.SelectTCoordArray = 'None'
resampleToImage4Display.TextureTransform = 'Transform2'
resampleToImage4Display.OSPRayScaleArray = 'scalars'
resampleToImage4Display.OSPRayScaleFunction = 'Piecewise Function'
resampleToImage4Display.Assembly = ''
resampleToImage4Display.SelectedBlockSelectors = ['']
resampleToImage4Display.SelectOrientationVectors = 'vectors'
resampleToImage4Display.ScaleFactor = 12.699987300000002
resampleToImage4Display.SelectScaleArray = 'scalars'
resampleToImage4Display.GlyphType = 'Arrow'
resampleToImage4Display.GlyphTableIndexArray = 'scalars'
resampleToImage4Display.GaussianRadius = 0.6349993650000001
resampleToImage4Display.SetScaleArray = ['POINTS', 'scalars']
resampleToImage4Display.ScaleTransferFunction = 'Piecewise Function'
resampleToImage4Display.OpacityArray = ['POINTS', 'scalars']
resampleToImage4Display.OpacityTransferFunction = 'Piecewise Function'
resampleToImage4Display.DataAxesGrid = 'Grid Axes Representation'
resampleToImage4Display.PolarAxes = 'Polar Axes Representation'
resampleToImage4Display.ScalarOpacityUnitDistance = 1.1053780532200748
resampleToImage4Display.OpacityArrayName = ['POINTS', 'scalars']
resampleToImage4Display.ColorArray2Name = ['POINTS', 'scalars']
resampleToImage4Display.IsosurfaceValues = [247.03096881201947]
resampleToImage4Display.SliceFunction = 'Plane'
resampleToImage4Display.Slice = 99
resampleToImage4Display.SelectInputVectors = ['POINTS', 'vectors']
resampleToImage4Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
resampleToImage4Display.ScaleTransferFunction.Points = [1.5401382081971097e-07, 0.0, 0.5, 0.0, 494.0619374700251, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
resampleToImage4Display.OpacityTransferFunction.Points = [1.5401382081971097e-07, 0.0, 0.5, 0.0, 494.0619374700251, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
resampleToImage4Display.SliceFunction.Origin = [7.105427357601002e-15, 7.105427357601002e-15, 7.105427357601002e-15]

# setup the color legend parameters for each legend in this view

# get color legend/bar for scalarsLUT in view renderView1
scalarsLUTColorBar = GetScalarBar(scalarsLUT, renderView1)
scalarsLUTColorBar.Title = 'scalars'
scalarsLUTColorBar.ComponentTitle = ''

# set color bar visibility
scalarsLUTColorBar.Visibility = 1

# show color legend
resampleToImage1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation scene

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.ViewModules = renderView1
animationScene1.Cues = timeAnimationCue1
animationScene1.AnimationTime = 0.0

# ----------------------------------------------------------------
# restore active source
SetActiveSource(resampleToImage1)
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