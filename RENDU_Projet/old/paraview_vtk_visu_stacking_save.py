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
renderView1.ViewSize = [1216, 780]
renderView1.AxesGrid = 'Grid Axes 3D Actor'
renderView1.CenterOfRotation = [7.105427357601002e-15, 0.0, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [327.95279349644255, 623.6763880086094, 264.9898072804633]
renderView1.CameraFocalPoint = [7.10542735760102e-15, 5.063731845458105e-29, 1.8945950887422214e-29]
renderView1.CameraViewUp = [0.8978781396077968, -0.3723203954947234, -0.23493056317366343]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 109.98511629539742
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
layout1.SetSize(1216, 780)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Legacy VTK Reader'
sag_GREvtk = LegacyVTKReader(registrationName='Sag_GRE.vtk', FileNames=['C:\\Users\\Utilisateur\\Documents\\CHPS0905\\Projet\\Projet_CHPS0905\\Projet2025\\VTK_Files\\Sag_GRE.vtk'])

# create a new 'Transform'
transform1 = Transform(registrationName='Transform1', Input=sag_GREvtk)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Translate = [158.81359379155964, -152.69545670902767, 26.73034817817157]
transform1.Transform.Rotate = [-87.86947394868992, -155.15774670652084, -73.65345489026272]
transform1.Transform.Scale = [1.000000000000005, 1.000000000000007, 1.0000000000000147]

# create a new 'Resample To Image'
resampleToImage1 = ResampleToImage(registrationName='ResampleToImage1', Input=transform1)
resampleToImage1.SamplingDimensions = [350, 350, 350]
resampleToImage1.SamplingBounds = [-63.5, 63.5, -63.5, 63.5, -63.5, 63.5]

# create a new 'XML Unstructured Grid Reader'
stokesvtu = XMLUnstructuredGridReader(registrationName='Stokes.vtu', FileName=['C:\\Users\\Utilisateur\\Documents\\CHPS0905\\Projet\\Projet_CHPS0905\\Projet2025\\VTK_Files\\Stokes.vtu'])
stokesvtu.CellArrayStatus = ['Label']
stokesvtu.PointArrayStatus = ['Velocity', 'Pressure']
stokesvtu.TimeArray = 'None'

# create a new 'Legacy VTK Reader'
ax_3DTOFvtk = LegacyVTKReader(registrationName='Ax_3DTOF.vtk', FileNames=['C:\\Users\\Utilisateur\\Documents\\CHPS0905\\Projet\\Projet_CHPS0905\\Projet2025\\VTK_Files\\Ax_3DTOF.vtk'])

# create a new 'Legacy VTK Reader'
sag_Fluxvtk = LegacyVTKReader(registrationName='Sag_Flux.vtk', FileNames=['C:\\Users\\Utilisateur\\Documents\\CHPS0905\\Projet\\Projet_CHPS0905\\Projet2025\\VTK_Files\\Sag_Flux.vtk'])

# create a new 'Transform'
transform4 = Transform(registrationName='Transform4', Input=sag_Fluxvtk)
transform4.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform4.Transform.Translate = [-129.2754, -26.714699999999997, -175.078]

# create a new 'Resample To Image'
resampleToImage4 = ResampleToImage(registrationName='ResampleToImage4', Input=transform4)
resampleToImage4.SamplingDimensions = [350, 350, 350]
resampleToImage4.SamplingBounds = [-63.499999999999986, 63.5, -63.5, 63.5, -63.5, 63.5]

# create a new 'Transform'
transform2 = Transform(registrationName='Transform2', Input=ax_3DTOFvtk)
transform2.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform2.Transform.Translate = [-1.4200733900070048, -23.332691192626996, -57.26286315917986]

# create a new 'Resample To Image'
resampleToImage2 = ResampleToImage(registrationName='ResampleToImage2', Input=transform2)
resampleToImage2.SamplingDimensions = [350, 350, 350]
resampleToImage2.SamplingBounds = [-76.25, 76.25, -95.75, 95.75, -63.250000000000156, 63.250000000000156]

# create a new 'Transform'
transform3 = Transform(registrationName='Transform3', Input=stokesvtu)
transform3.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform3.Transform.Translate = [32.2577922710919, -201.70469507593393, 100.85788283905518]
transform3.Transform.Rotate = [-77.05886247385291, 87.72172014887698, 80.51077186824962]
transform3.Transform.Scale = [1.0000000000000708, 1.000000000000026, 1.0000000000000984]

# create a new 'Resample To Image'
resampleToImage3 = ResampleToImage(registrationName='ResampleToImage3', Input=transform3)
resampleToImage3.SamplingDimensions = [350, 350, 350]
resampleToImage3.SamplingBounds = [-30.453418731689453, 30.453418731689453, -71.47843933105469, 71.47843933105469, -20.005020141601562, 20.005020141601562]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from resampleToImage1
resampleToImage1Display = Show(resampleToImage1, renderView1, 'UniformGridRepresentation')

# get separate 2D transfer function for 'scalars'
separate_resampleToImage1Display_scalarsTF2D = GetTransferFunction2D('scalars', resampleToImage1Display, separate=True)
separate_resampleToImage1Display_scalarsTF2D.ScalarRangeInitialized = 1
separate_resampleToImage1Display_scalarsTF2D.Range = [0.0, 167.0, 0.0, 1.0]

# get separate color transfer function/color map for 'scalars'
separate_resampleToImage1Display_scalarsLUT = GetColorTransferFunction('scalars', resampleToImage1Display, separate=True)
separate_resampleToImage1Display_scalarsLUT.TransferFunction2D = separate_resampleToImage1Display_scalarsTF2D
separate_resampleToImage1Display_scalarsLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 87.5, 0.865003, 0.865003, 0.865003, 175.0, 0.705882, 0.0156863, 0.14902]
separate_resampleToImage1Display_scalarsLUT.ShowDataHistogram = 1
separate_resampleToImage1Display_scalarsLUT.ScalarRangeInitialized = 1.0

# get separate opacity transfer function/opacity map for 'scalars'
separate_resampleToImage1Display_scalarsPWF = GetOpacityTransferFunction('scalars', resampleToImage1Display, separate=True)
separate_resampleToImage1Display_scalarsPWF.Points = [0.0, 0.0, 0.5, 0.0, 28.731344417183696, 0.0, 0.5, 0.0, 175.0, 1.0, 0.5, 0.0]
separate_resampleToImage1Display_scalarsPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
resampleToImage1Display.Representation = 'Volume'
resampleToImage1Display.ColorArrayName = ['POINTS', 'scalars']
resampleToImage1Display.LookupTable = separate_resampleToImage1Display_scalarsLUT
resampleToImage1Display.SelectNormalArray = 'None'
resampleToImage1Display.SelectTangentArray = 'None'
resampleToImage1Display.SelectTCoordArray = 'None'
resampleToImage1Display.TextureTransform = 'Transform2'
resampleToImage1Display.OSPRayScaleArray = 'scalars'
resampleToImage1Display.OSPRayScaleFunction = 'Piecewise Function'
resampleToImage1Display.Assembly = ''
resampleToImage1Display.SelectedBlockSelectors = ['']
resampleToImage1Display.SelectOrientationVectors = 'None'
resampleToImage1Display.ScaleFactor = 12.6999873
resampleToImage1Display.SelectScaleArray = 'scalars'
resampleToImage1Display.GlyphType = 'Arrow'
resampleToImage1Display.GlyphTableIndexArray = 'scalars'
resampleToImage1Display.GaussianRadius = 0.634999365
resampleToImage1Display.SetScaleArray = ['POINTS', 'scalars']
resampleToImage1Display.ScaleTransferFunction = 'Piecewise Function'
resampleToImage1Display.OpacityArray = ['POINTS', 'scalars']
resampleToImage1Display.OpacityTransferFunction = 'Piecewise Function'
resampleToImage1Display.DataAxesGrid = 'Grid Axes Representation'
resampleToImage1Display.PolarAxes = 'Polar Axes Representation'
resampleToImage1Display.ScalarOpacityUnitDistance = 0.6302871994005582
resampleToImage1Display.ScalarOpacityFunction = separate_resampleToImage1Display_scalarsPWF
resampleToImage1Display.TransferFunction2D = separate_resampleToImage1Display_scalarsTF2D
resampleToImage1Display.OpacityArrayName = ['POINTS', 'scalars']
resampleToImage1Display.ColorArray2Name = ['POINTS', 'scalars']
resampleToImage1Display.IsosurfaceValues = [83.5]
resampleToImage1Display.SliceFunction = 'Plane'
resampleToImage1Display.Slice = 174
resampleToImage1Display.SelectInputVectors = [None, '']
resampleToImage1Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
resampleToImage1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 167.0, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
resampleToImage1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 167.0, 1.0, 0.5, 0.0]

# set separate color map
resampleToImage1Display.UseSeparateColorMap = True

# show data from resampleToImage2
resampleToImage2Display = Show(resampleToImage2, renderView1, 'UniformGridRepresentation')

# get separate 2D transfer function for 'scalars'
separate_resampleToImage2Display_scalarsTF2D = GetTransferFunction2D('scalars', resampleToImage2Display, separate=True)
separate_resampleToImage2Display_scalarsTF2D.ScalarRangeInitialized = 1
separate_resampleToImage2Display_scalarsTF2D.Range = [0.0, 737.0, 0.0, 1.0]

# get separate color transfer function/color map for 'scalars'
separate_resampleToImage2Display_scalarsLUT = GetColorTransferFunction('scalars', resampleToImage2Display, separate=True)
separate_resampleToImage2Display_scalarsLUT.TransferFunction2D = separate_resampleToImage2Display_scalarsTF2D
separate_resampleToImage2Display_scalarsLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 368.5, 0.865003, 0.865003, 0.865003, 737.0, 0.705882, 0.0156863, 0.14902]
separate_resampleToImage2Display_scalarsLUT.ShowDataHistogram = 1
separate_resampleToImage2Display_scalarsLUT.ScalarRangeInitialized = 1.0

# get separate opacity transfer function/opacity map for 'scalars'
separate_resampleToImage2Display_scalarsPWF = GetOpacityTransferFunction('scalars', resampleToImage2Display, separate=True)
separate_resampleToImage2Display_scalarsPWF.Points = [0.0, 0.0, 0.5, 0.0, 116.60000610351562, 0.0, 0.5, 0.0, 737.0, 1.0, 0.5, 0.0]
separate_resampleToImage2Display_scalarsPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
resampleToImage2Display.Representation = 'Volume'
resampleToImage2Display.ColorArrayName = ['POINTS', 'scalars']
resampleToImage2Display.LookupTable = separate_resampleToImage2Display_scalarsLUT
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
resampleToImage2Display.ScalarOpacityUnitDistance = 0.7895560824838618
resampleToImage2Display.ScalarOpacityFunction = separate_resampleToImage2Display_scalarsPWF
resampleToImage2Display.TransferFunction2D = separate_resampleToImage2Display_scalarsTF2D
resampleToImage2Display.OpacityArrayName = ['POINTS', 'scalars']
resampleToImage2Display.ColorArray2Name = ['POINTS', 'scalars']
resampleToImage2Display.IsosurfaceValues = [368.5]
resampleToImage2Display.SliceFunction = 'Plane'
resampleToImage2Display.Slice = 174
resampleToImage2Display.SelectInputVectors = [None, '']
resampleToImage2Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
resampleToImage2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 737.0, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
resampleToImage2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 737.0, 1.0, 0.5, 0.0]

# set separate color map
resampleToImage2Display.UseSeparateColorMap = True

# show data from resampleToImage3
resampleToImage3Display = Show(resampleToImage3, renderView1, 'UniformGridRepresentation')

# get 2D transfer function for 'Velocity'
velocityTF2D = GetTransferFunction2D('Velocity')
velocityTF2D.ScalarRangeInitialized = 1
velocityTF2D.Range = [8.678034256429184e-37, 2841.4608187306544, 0.0, 1.0]

# get color transfer function/color map for 'Velocity'
velocityLUT = GetColorTransferFunction('Velocity')
velocityLUT.TransferFunction2D = velocityTF2D
velocityLUT.RGBPoints = [8.869892004874882e-38, 0.231373, 0.298039, 0.752941, 1493.1973832111867, 0.865003, 0.865003, 0.865003, 2986.3947664223733, 0.705882, 0.0156863, 0.14902]
velocityLUT.ShowDataHistogram = 1
velocityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Velocity'
velocityPWF = GetOpacityTransferFunction('Velocity')
velocityPWF.Points = [8.869892004874882e-38, 0.0, 0.5, 0.0, 2986.3947664223733, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
resampleToImage3Display.Representation = 'Volume'
resampleToImage3Display.ColorArrayName = ['POINTS', 'Velocity']
resampleToImage3Display.LookupTable = velocityLUT
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
resampleToImage3Display.ScalarOpacityUnitDistance = 0.45976766862147966
resampleToImage3Display.ScalarOpacityFunction = velocityPWF
resampleToImage3Display.TransferFunction2D = velocityTF2D
resampleToImage3Display.OpacityArrayName = ['POINTS', 'Label']
resampleToImage3Display.ColorArray2Name = ['POINTS', 'Label']
resampleToImage3Display.SliceFunction = 'Plane'
resampleToImage3Display.Slice = 174
resampleToImage3Display.SelectInputVectors = ['POINTS', 'Velocity']
resampleToImage3Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
resampleToImage3Display.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 6.0, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
resampleToImage3Display.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 6.0, 1.0, 0.5, 0.0]

# show data from resampleToImage4
resampleToImage4Display = Show(resampleToImage4, renderView1, 'UniformGridRepresentation')

# get separate 2D transfer function for 'vectors'
separate_resampleToImage4Display_vectorsTF2D = GetTransferFunction2D('vectors', resampleToImage4Display, separate=True)
separate_resampleToImage4Display_vectorsTF2D.ScalarRangeInitialized = 1
separate_resampleToImage4Display_vectorsTF2D.Range = [6.761510431591073e-08, 494.22225986117024, 0.0, 1.0]

# get separate color transfer function/color map for 'vectors'
separate_resampleToImage4Display_vectorsLUT = GetColorTransferFunction('vectors', resampleToImage4Display, separate=True)
separate_resampleToImage4Display_vectorsLUT.TransferFunction2D = separate_resampleToImage4Display_vectorsTF2D
separate_resampleToImage4Display_vectorsLUT.RGBPoints = [6.761510431591073e-08, 0.231373, 0.298039, 0.752941, 247.1111299643927, 0.865003, 0.865003, 0.865003, 494.22225986117024, 0.705882, 0.0156863, 0.14902]
separate_resampleToImage4Display_vectorsLUT.ShowDataHistogram = 1
separate_resampleToImage4Display_vectorsLUT.ScalarRangeInitialized = 1.0

# get separate opacity transfer function/opacity map for 'vectors'
separate_resampleToImage4Display_vectorsPWF = GetOpacityTransferFunction('vectors', resampleToImage4Display, separate=True)
separate_resampleToImage4Display_vectorsPWF.Points = [6.761510431591073e-08, 0.0, 0.5, 0.0, 184.41128552713909, 0.0, 0.5, 0.0, 240.47232072192062, 0.0, 0.5, 0.0, 494.22225986117024, 0.9955357313156128, 0.5, 0.0]
separate_resampleToImage4Display_vectorsPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
resampleToImage4Display.Representation = 'Volume'
resampleToImage4Display.ColorArrayName = ['POINTS', 'vectors']
resampleToImage4Display.LookupTable = separate_resampleToImage4Display_vectorsLUT
resampleToImage4Display.SelectNormalArray = 'None'
resampleToImage4Display.SelectTangentArray = 'None'
resampleToImage4Display.SelectTCoordArray = 'None'
resampleToImage4Display.TextureTransform = 'Transform2'
resampleToImage4Display.OSPRayScaleArray = 'scalars'
resampleToImage4Display.OSPRayScaleFunction = 'Piecewise Function'
resampleToImage4Display.Assembly = ''
resampleToImage4Display.SelectedBlockSelectors = ['']
resampleToImage4Display.SelectOrientationVectors = 'vectors'
resampleToImage4Display.ScaleFactor = 12.6999873
resampleToImage4Display.SelectScaleArray = 'scalars'
resampleToImage4Display.GlyphType = 'Arrow'
resampleToImage4Display.GlyphTableIndexArray = 'scalars'
resampleToImage4Display.GaussianRadius = 0.634999365
resampleToImage4Display.SetScaleArray = ['POINTS', 'scalars']
resampleToImage4Display.ScaleTransferFunction = 'Piecewise Function'
resampleToImage4Display.OpacityArray = ['POINTS', 'scalars']
resampleToImage4Display.OpacityTransferFunction = 'Piecewise Function'
resampleToImage4Display.DataAxesGrid = 'Grid Axes Representation'
resampleToImage4Display.PolarAxes = 'Polar Axes Representation'
resampleToImage4Display.ScalarOpacityUnitDistance = 0.6302871994005582
resampleToImage4Display.ScalarOpacityFunction = separate_resampleToImage4Display_vectorsPWF
resampleToImage4Display.TransferFunction2D = separate_resampleToImage4Display_vectorsTF2D
resampleToImage4Display.OpacityArrayName = ['POINTS', 'scalars']
resampleToImage4Display.ColorArray2Name = ['POINTS', 'scalars']
resampleToImage4Display.IsosurfaceValues = [249.3686473282981]
resampleToImage4Display.SliceFunction = 'Plane'
resampleToImage4Display.Slice = 174
resampleToImage4Display.SelectInputVectors = ['POINTS', 'vectors']
resampleToImage4Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
resampleToImage4Display.ScaleTransferFunction.Points = [1.7756552672785487e-07, 0.0, 0.5, 0.0, 498.73729447903065, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
resampleToImage4Display.OpacityTransferFunction.Points = [1.7756552672785487e-07, 0.0, 0.5, 0.0, 498.73729447903065, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
resampleToImage4Display.SliceFunction.Origin = [7.105427357601002e-15, 0.0, 0.0]

# set separate color map
resampleToImage4Display.UseSeparateColorMap = True

# show data from sag_Fluxvtk
sag_FluxvtkDisplay = Show(sag_Fluxvtk, renderView1, 'UniformGridRepresentation')

# get separate 2D transfer function for 'scalars'
separate_sag_FluxvtkDisplay_scalarsTF2D = GetTransferFunction2D('scalars', sag_FluxvtkDisplay, separate=True)
separate_sag_FluxvtkDisplay_scalarsTF2D.ScalarRangeInitialized = 1
separate_sag_FluxvtkDisplay_scalarsTF2D.Range = [0.0, 515.6464233398438, 0.0, 1.0]

# get separate color transfer function/color map for 'scalars'
separate_sag_FluxvtkDisplay_scalarsLUT = GetColorTransferFunction('scalars', sag_FluxvtkDisplay, separate=True)
separate_sag_FluxvtkDisplay_scalarsLUT.TransferFunction2D = separate_sag_FluxvtkDisplay_scalarsTF2D
separate_sag_FluxvtkDisplay_scalarsLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 257.8232116699219, 0.865003, 0.865003, 0.865003, 515.6464233398438, 0.705882, 0.0156863, 0.14902]
separate_sag_FluxvtkDisplay_scalarsLUT.ShowDataHistogram = 1
separate_sag_FluxvtkDisplay_scalarsLUT.ScalarRangeInitialized = 1.0

# get separate opacity transfer function/opacity map for 'scalars'
separate_sag_FluxvtkDisplay_scalarsPWF = GetOpacityTransferFunction('scalars', sag_FluxvtkDisplay, separate=True)
separate_sag_FluxvtkDisplay_scalarsPWF.Points = [0.0, 0.0, 0.5, 0.0, 346.3297119140625, 0.0, 0.5, 0.0, 515.6464233398438, 1.0, 0.5, 0.0]
separate_sag_FluxvtkDisplay_scalarsPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
sag_FluxvtkDisplay.Representation = 'Volume'
sag_FluxvtkDisplay.ColorArrayName = ['POINTS', 'scalars']
sag_FluxvtkDisplay.LookupTable = separate_sag_FluxvtkDisplay_scalarsLUT
sag_FluxvtkDisplay.SelectNormalArray = 'None'
sag_FluxvtkDisplay.SelectTangentArray = 'None'
sag_FluxvtkDisplay.SelectTCoordArray = 'None'
sag_FluxvtkDisplay.TextureTransform = 'Transform2'
sag_FluxvtkDisplay.OSPRayScaleArray = 'scalars'
sag_FluxvtkDisplay.OSPRayScaleFunction = 'Piecewise Function'
sag_FluxvtkDisplay.Assembly = ''
sag_FluxvtkDisplay.SelectedBlockSelectors = ['']
sag_FluxvtkDisplay.SelectOrientationVectors = 'vectors'
sag_FluxvtkDisplay.ScaleFactor = 12.700000000000001
sag_FluxvtkDisplay.SelectScaleArray = 'scalars'
sag_FluxvtkDisplay.GlyphType = 'Arrow'
sag_FluxvtkDisplay.GlyphTableIndexArray = 'scalars'
sag_FluxvtkDisplay.GaussianRadius = 0.635
sag_FluxvtkDisplay.SetScaleArray = ['POINTS', 'scalars']
sag_FluxvtkDisplay.ScaleTransferFunction = 'Piecewise Function'
sag_FluxvtkDisplay.OpacityArray = ['POINTS', 'scalars']
sag_FluxvtkDisplay.OpacityTransferFunction = 'Piecewise Function'
sag_FluxvtkDisplay.DataAxesGrid = 'Grid Axes Representation'
sag_FluxvtkDisplay.PolarAxes = 'Polar Axes Representation'
sag_FluxvtkDisplay.ScalarOpacityUnitDistance = 1.732050807568877
sag_FluxvtkDisplay.ScalarOpacityFunction = separate_sag_FluxvtkDisplay_scalarsPWF
sag_FluxvtkDisplay.TransferFunction2D = separate_sag_FluxvtkDisplay_scalarsTF2D
sag_FluxvtkDisplay.OpacityArrayName = ['POINTS', 'scalars']
sag_FluxvtkDisplay.ColorArray2Name = ['POINTS', 'scalars']
sag_FluxvtkDisplay.IsosurfaceValues = [257.8232116699219]
sag_FluxvtkDisplay.SliceFunction = 'Plane'
sag_FluxvtkDisplay.Slice = 63
sag_FluxvtkDisplay.SelectInputVectors = ['POINTS', 'vectors']
sag_FluxvtkDisplay.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
sag_FluxvtkDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 515.6464233398438, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
sag_FluxvtkDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 515.6464233398438, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
sag_FluxvtkDisplay.SliceFunction.Origin = [129.2754, 26.714699999999997, 175.078]

# set separate color map
sag_FluxvtkDisplay.UseSeparateColorMap = True

# setup the color legend parameters for each legend in this view

# get 2D transfer function for 'scalars'
scalarsTF2D = GetTransferFunction2D('scalars')
scalarsTF2D.ScalarRangeInitialized = 1
scalarsTF2D.Range = [0.0, 515.6464233398438, 0.0, 1.0]

# get color transfer function/color map for 'scalars'
scalarsLUT = GetColorTransferFunction('scalars')
scalarsLUT.TransferFunction2D = scalarsTF2D
scalarsLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 368.5, 0.865003, 0.865003, 0.865003, 737.0, 0.705882, 0.0156863, 0.14902]
scalarsLUT.ShowDataHistogram = 1
scalarsLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for scalarsLUT in view renderView1
scalarsLUTColorBar = GetScalarBar(scalarsLUT, renderView1)
scalarsLUTColorBar.Title = 'scalars'
scalarsLUTColorBar.ComponentTitle = ''

# set color bar visibility
scalarsLUTColorBar.Visibility = 0

# get color legend/bar for separate_resampleToImage1Display_scalarsLUT in view renderView1
separate_resampleToImage1Display_scalarsLUTColorBar = GetScalarBar(separate_resampleToImage1Display_scalarsLUT, renderView1)
separate_resampleToImage1Display_scalarsLUTColorBar.WindowLocation = 'Any Location'
separate_resampleToImage1Display_scalarsLUTColorBar.Position = [0.00986842105263154, 0.2666666666666667]
separate_resampleToImage1Display_scalarsLUTColorBar.Title = 'scalars'
separate_resampleToImage1Display_scalarsLUTColorBar.ComponentTitle = ''
separate_resampleToImage1Display_scalarsLUTColorBar.ScalarBarLength = 0.32999999999999996

# set color bar visibility
separate_resampleToImage1Display_scalarsLUTColorBar.Visibility = 1

# get color legend/bar for separate_resampleToImage2Display_scalarsLUT in view renderView1
separate_resampleToImage2Display_scalarsLUTColorBar = GetScalarBar(separate_resampleToImage2Display_scalarsLUT, renderView1)
separate_resampleToImage2Display_scalarsLUTColorBar.WindowLocation = 'Any Location'
separate_resampleToImage2Display_scalarsLUTColorBar.Position = [0.8371710526315789, 0.03717948717948716]
separate_resampleToImage2Display_scalarsLUTColorBar.Title = 'scalars'
separate_resampleToImage2Display_scalarsLUTColorBar.ComponentTitle = ''
separate_resampleToImage2Display_scalarsLUTColorBar.ScalarBarLength = 0.33000000000000007

# set color bar visibility
separate_resampleToImage2Display_scalarsLUTColorBar.Visibility = 1

# get 2D transfer function for 'Label'
labelTF2D = GetTransferFunction2D('Label')
labelTF2D.ScalarRangeInitialized = 1
labelTF2D.Range = [1.0, 6.0, 0.0, 1.0]

# get color transfer function/color map for 'Label'
labelLUT = GetColorTransferFunction('Label')
labelLUT.TransferFunction2D = labelTF2D
labelLUT.RGBPoints = [1.0, 0.231373, 0.298039, 0.752941, 3.5, 0.865003, 0.865003, 0.865003, 6.0, 0.705882, 0.0156863, 0.14902]
labelLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for labelLUT in view renderView1
labelLUTColorBar = GetScalarBar(labelLUT, renderView1)
labelLUTColorBar.Title = 'Label'
labelLUTColorBar.ComponentTitle = ''

# set color bar visibility
labelLUTColorBar.Visibility = 0

# get color legend/bar for velocityLUT in view renderView1
velocityLUTColorBar = GetScalarBar(velocityLUT, renderView1)
velocityLUTColorBar.WindowLocation = 'Upper Right Corner'
velocityLUTColorBar.Title = 'Velocity'
velocityLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
velocityLUTColorBar.Visibility = 1

# get 2D transfer function for 'Pressure'
pressureTF2D = GetTransferFunction2D('Pressure')
pressureTF2D.ScalarRangeInitialized = 1
pressureTF2D.Range = [0.7553926314317794, 2.0292678740192183, 0.0, 1.0]

# get color transfer function/color map for 'Pressure'
pressureLUT = GetColorTransferFunction('Pressure')
pressureLUT.TransferFunction2D = pressureTF2D
pressureLUT.RGBPoints = [0.7553926314317794, 0.231373, 0.298039, 0.752941, 1.3923302527254988, 0.865003, 0.865003, 0.865003, 2.0292678740192183, 0.705882, 0.0156863, 0.14902]
pressureLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for pressureLUT in view renderView1
pressureLUTColorBar = GetScalarBar(pressureLUT, renderView1)
pressureLUTColorBar.Title = 'Pressure'
pressureLUTColorBar.ComponentTitle = ''

# set color bar visibility
pressureLUTColorBar.Visibility = 0

# get separate 2D transfer function for 'scalars'
separate_resampleToImage4Display_scalarsTF2D = GetTransferFunction2D('scalars', resampleToImage4Display, separate=True)
separate_resampleToImage4Display_scalarsTF2D.ScalarRangeInitialized = 1
separate_resampleToImage4Display_scalarsTF2D.Range = [1.7756552672785487e-07, 498.73729447903065, 0.0, 1.0]

# get separate color transfer function/color map for 'scalars'
separate_resampleToImage4Display_scalarsLUT = GetColorTransferFunction('scalars', resampleToImage4Display, separate=True)
separate_resampleToImage4Display_scalarsLUT.TransferFunction2D = separate_resampleToImage4Display_scalarsTF2D
separate_resampleToImage4Display_scalarsLUT.RGBPoints = [1.7756552672785487e-07, 0.231373, 0.298039, 0.752941, 249.3686473282981, 0.865003, 0.865003, 0.865003, 498.73729447903065, 0.705882, 0.0156863, 0.14902]
separate_resampleToImage4Display_scalarsLUT.ShowDataHistogram = 1
separate_resampleToImage4Display_scalarsLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for separate_resampleToImage4Display_scalarsLUT in view renderView1
separate_resampleToImage4Display_scalarsLUTColorBar = GetScalarBar(separate_resampleToImage4Display_scalarsLUT, renderView1)
separate_resampleToImage4Display_scalarsLUTColorBar.Title = 'scalars'
separate_resampleToImage4Display_scalarsLUTColorBar.ComponentTitle = ''

# set color bar visibility
separate_resampleToImage4Display_scalarsLUTColorBar.Visibility = 0

# get color legend/bar for separate_resampleToImage4Display_vectorsLUT in view renderView1
separate_resampleToImage4Display_vectorsLUTColorBar = GetScalarBar(separate_resampleToImage4Display_vectorsLUT, renderView1)
separate_resampleToImage4Display_vectorsLUTColorBar.WindowLocation = 'Upper Left Corner'
separate_resampleToImage4Display_vectorsLUTColorBar.Position = [0.003289473684210526, 0.6538461538461539]
separate_resampleToImage4Display_vectorsLUTColorBar.Title = 'vectors'
separate_resampleToImage4Display_vectorsLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
separate_resampleToImage4Display_vectorsLUTColorBar.Visibility = 1

# get 2D transfer function for 'DICOMImage'
dICOMImageTF2D = GetTransferFunction2D('DICOMImage')
dICOMImageTF2D.ScalarRangeInitialized = 1
dICOMImageTF2D.Range = [0.0, 482.0, 0.0, 1.0]

# get color transfer function/color map for 'DICOMImage'
dICOMImageLUT = GetColorTransferFunction('DICOMImage')
dICOMImageLUT.TransferFunction2D = dICOMImageTF2D
dICOMImageLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 241.0, 0.865003, 0.865003, 0.865003, 482.0, 0.705882, 0.0156863, 0.14902]
dICOMImageLUT.ShowDataHistogram = 1
dICOMImageLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for dICOMImageLUT in view renderView1
dICOMImageLUTColorBar = GetScalarBar(dICOMImageLUT, renderView1)
dICOMImageLUTColorBar.Title = 'DICOMImage'
dICOMImageLUTColorBar.ComponentTitle = ''

# set color bar visibility
dICOMImageLUTColorBar.Visibility = 0

# get 2D transfer function for 'Separate_14100_DICOMImage'
separate_14100_DICOMImageTF2D = GetTransferFunction2D('Separate_14100_DICOMImage')
separate_14100_DICOMImageTF2D.ScalarRangeInitialized = 1
separate_14100_DICOMImageTF2D.Range = [0.0, 446.0, 0.0, 1.0]

# get color transfer function/color map for 'Separate_14100_DICOMImage'
separate_14100_DICOMImageLUT = GetColorTransferFunction('Separate_14100_DICOMImage')
separate_14100_DICOMImageLUT.TransferFunction2D = separate_14100_DICOMImageTF2D
separate_14100_DICOMImageLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 230.0, 0.865003, 0.865003, 0.865003, 460.0, 0.705882, 0.0156863, 0.14902]
separate_14100_DICOMImageLUT.ShowDataHistogram = 1
separate_14100_DICOMImageLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for separate_14100_DICOMImageLUT in view renderView1
separate_14100_DICOMImageLUTColorBar = GetScalarBar(separate_14100_DICOMImageLUT, renderView1)
separate_14100_DICOMImageLUTColorBar.Title = 'DICOMImage'
separate_14100_DICOMImageLUTColorBar.ComponentTitle = ''

# set color bar visibility
separate_14100_DICOMImageLUTColorBar.Visibility = 0

# get color legend/bar for separate_sag_FluxvtkDisplay_scalarsLUT in view renderView1
separate_sag_FluxvtkDisplay_scalarsLUTColorBar = GetScalarBar(separate_sag_FluxvtkDisplay_scalarsLUT, renderView1)
separate_sag_FluxvtkDisplay_scalarsLUTColorBar.Title = 'scalars'
separate_sag_FluxvtkDisplay_scalarsLUTColorBar.ComponentTitle = ''

# set color bar visibility
separate_sag_FluxvtkDisplay_scalarsLUTColorBar.Visibility = 0

# show color legend
resampleToImage1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
resampleToImage2Display.SetScalarBarVisibility(renderView1, True)

# show color legend
resampleToImage3Display.SetScalarBarVisibility(renderView1, True)

# show color legend
resampleToImage4Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(sag_Fluxvtk, renderView1)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get separate opacity transfer function/opacity map for 'scalars'
separate_resampleToImage4Display_scalarsPWF = GetOpacityTransferFunction('scalars', resampleToImage4Display, separate=True)
separate_resampleToImage4Display_scalarsPWF.Points = [1.7756552672785487e-07, 0.0, 0.5, 0.0, 1.7756552672785487e-07, 0.0, 0.5, 0.0, 1.7756552672785487e-07, 1.0, 0.5, 0.0, 1.7756552672785487e-07, 0.0, 0.5, 0.0, 49.12934875488281, 0.0, 0.5, 0.0, 99.7474594116211, 0.0, 0.5, 0.0, 147.38804626464844, 0.0, 0.5, 0.0, 498.73729447903065, 0.3482142984867096, 0.5, 0.0]
separate_resampleToImage4Display_scalarsPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'Pressure'
pressurePWF = GetOpacityTransferFunction('Pressure')
pressurePWF.Points = [0.7553926314317794, 0.0, 0.5, 0.0, 2.0292678740192183, 1.0, 0.5, 0.0]
pressurePWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'scalars'
scalarsPWF = GetOpacityTransferFunction('scalars')
scalarsPWF.Points = [0.0, 0.0, 0.5, 0.0, 145.1999969482422, 0.0, 0.5, 0.0, 737.0, 1.0, 0.5, 0.0]
scalarsPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'Separate_14100_DICOMImage'
separate_14100_DICOMImagePWF = GetOpacityTransferFunction('Separate_14100_DICOMImage')
separate_14100_DICOMImagePWF.Points = [0.0, 0.0, 0.5, 0.0, 134.5671717896055, 0.0, 0.5, 0.0, 460.0, 1.0, 0.5, 0.0]
separate_14100_DICOMImagePWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'DICOMImage'
dICOMImagePWF = GetOpacityTransferFunction('DICOMImage')
dICOMImagePWF.Points = [0.0, 0.0, 0.5, 0.0, 191.36119079589844, 0.0, 0.5, 0.0, 482.0, 1.0, 0.5, 0.0]
dICOMImagePWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'Label'
labelPWF = GetOpacityTransferFunction('Label')
labelPWF.Points = [1.0, 0.0, 0.5, 0.0, 6.0, 1.0, 0.5, 0.0]
labelPWF.ScalarRangeInitialized = 1

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
SetActiveSource(sag_Fluxvtk)
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