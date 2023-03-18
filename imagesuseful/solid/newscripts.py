# trace generated using paraview version 5.11.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
fluidfoam = OpenFOAMReader(registrationName='fluid.foam', FileName='/media/Hengzhu/DRIVE3:DATAH/solid/2.0/fluid.foam')
fluidfoam.MeshRegions = ['internalMesh']

# Properties modified on fluidfoam
fluidfoam.SkipZeroTime = 0
fluidfoam.CaseType = 'Decomposed Case'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
fluidfoamDisplay = Show(fluidfoam, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'p'
pTF2D = GetTransferFunction2D('p')

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')
pLUT.TransferFunction2D = pTF2D
pLUT.RGBPoints = [1000.0, 0.231373, 0.298039, 0.752941, 553127988.0, 0.865003, 0.865003, 0.865003, 1106254976.0, 0.705882, 0.0156863, 0.14902]
pLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')
pPWF.Points = [1000.0, 0.0, 0.5, 0.0, 1106254976.0, 1.0, 0.5, 0.0]
pPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
fluidfoamDisplay.Representation = 'Surface'
fluidfoamDisplay.ColorArrayName = ['POINTS', 'p']
fluidfoamDisplay.LookupTable = pLUT
fluidfoamDisplay.SelectTCoordArray = 'None'
fluidfoamDisplay.SelectNormalArray = 'None'
fluidfoamDisplay.SelectTangentArray = 'None'
fluidfoamDisplay.OSPRayScaleArray = 'p'
fluidfoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
fluidfoamDisplay.SelectOrientationVectors = 'U'
fluidfoamDisplay.ScaleFactor = 0.0004999999888241291
fluidfoamDisplay.SelectScaleArray = 'p'
fluidfoamDisplay.GlyphType = 'Arrow'
fluidfoamDisplay.GlyphTableIndexArray = 'p'
fluidfoamDisplay.GaussianRadius = 2.4999999441206457e-05
fluidfoamDisplay.SetScaleArray = ['POINTS', 'p']
fluidfoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
fluidfoamDisplay.OpacityArray = ['POINTS', 'p']
fluidfoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
fluidfoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
fluidfoamDisplay.PolarAxes = 'PolarAxesRepresentation'
fluidfoamDisplay.ScalarOpacityFunction = pPWF
fluidfoamDisplay.ScalarOpacityUnitDistance = 7.90258737271368e-05
fluidfoamDisplay.OpacityArrayName = ['POINTS', 'p']
fluidfoamDisplay.SelectInputVectors = ['POINTS', 'U']
fluidfoamDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
fluidfoamDisplay.ScaleTransferFunction.Points = [101325.0, 0.0, 0.5, 0.0, 1091745024.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
fluidfoamDisplay.OpacityTransferFunction.Points = [101325.0, 0.0, 0.5, 0.0, 1091745024.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
fluidfoamDisplay.SetScalarBarVisibility(renderView1, True)

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [0.0024999999441206455, 0.0024999999441206455, 0.01366039389269756]
renderView1.CameraFocalPoint = [0.0024999999441206455, 0.0024999999441206455, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [0.0024999999441206455, 0.0024999999441206455, 0.01366039389269756]
renderView1.CameraFocalPoint = [0.0024999999441206455, 0.0024999999441206455, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [0.0024999999441206455, 0.0024999999441206455, 0.01366039389269756]
renderView1.CameraFocalPoint = [0.0024999999441206455, 0.0024999999441206455, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# set scalar coloring
ColorBy(fluidfoamDisplay, ('POINTS', 'U', 'Magnitude'))

# rescale color and/or opacity maps used to exactly fit the current data range
fluidfoamDisplay.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to include current data range
fluidfoamDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fluidfoamDisplay.SetScalarBarVisibility(renderView1, True)

# create a new 'Transform'
transform3 = Transform(registrationName='Transform3', Input=fluidfoam)
transform3.Transform = 'Transform'

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=transform3.Transform)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=transform3.Transform)

# show data in view
transform3Display = Show(transform3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
transform3Display.Representation = 'Surface'
transform3Display.ColorArrayName = ['POINTS', 'p']
transform3Display.LookupTable = pLUT
transform3Display.SelectTCoordArray = 'None'
transform3Display.SelectNormalArray = 'None'
transform3Display.SelectTangentArray = 'None'
transform3Display.OSPRayScaleArray = 'p'
transform3Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform3Display.SelectOrientationVectors = 'U'
transform3Display.ScaleFactor = 0.0004999999888241291
transform3Display.SelectScaleArray = 'p'
transform3Display.GlyphType = 'Arrow'
transform3Display.GlyphTableIndexArray = 'p'
transform3Display.GaussianRadius = 2.4999999441206457e-05
transform3Display.SetScaleArray = ['POINTS', 'p']
transform3Display.ScaleTransferFunction = 'PiecewiseFunction'
transform3Display.OpacityArray = ['POINTS', 'p']
transform3Display.OpacityTransferFunction = 'PiecewiseFunction'
transform3Display.DataAxesGrid = 'GridAxesRepresentation'
transform3Display.PolarAxes = 'PolarAxesRepresentation'
transform3Display.ScalarOpacityFunction = pPWF
transform3Display.ScalarOpacityUnitDistance = 7.90258737271368e-05
transform3Display.OpacityArrayName = ['POINTS', 'p']
transform3Display.SelectInputVectors = ['POINTS', 'U']
transform3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform3Display.ScaleTransferFunction.Points = [101325.0, 0.0, 0.5, 0.0, 1091745024.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform3Display.OpacityTransferFunction.Points = [101325.0, 0.0, 0.5, 0.0, 1091745024.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(fluidfoam, renderView1)

# show color bar/color legend
transform3Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(fluidfoam)

# show data in view
fluidfoamDisplay = Show(fluidfoam, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
fluidfoamDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring using an separate color/opacity maps
ColorBy(fluidfoamDisplay, ('POINTS', 'U', 'Magnitude'), True)

# rescale color and/or opacity maps used to exactly fit the current data range
fluidfoamDisplay.RescaleTransferFunctionToDataRange(False, True)

# get 2D transfer function for 'U'
uTF2D = GetTransferFunction2D('U')

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')
uLUT.TransferFunction2D = uTF2D
uLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 48.04509050868726, 0.865003, 0.865003, 0.865003, 96.09018101737452, 0.705882, 0.0156863, 0.14902]
uLUT.ScalarRangeInitialized = 1.0

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(uLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
fluidfoamDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fluidfoamDisplay.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(transform3)

# set scalar coloring using an separate color/opacity maps
ColorBy(transform3Display, ('POINTS', 'p'), True)

# rescale color and/or opacity maps used to exactly fit the current data range
transform3Display.RescaleTransferFunctionToDataRange(False, True)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
transform3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
transform3Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Contour'
contour5 = Contour(registrationName='Contour5', Input=transform3)
contour5.ContourBy = ['POINTS', 'p']
contour5.Isosurfaces = [545923174.5]
contour5.PointMergeMethod = 'Uniform Binning'

# show data in view
contour5Display = Show(contour5, renderView1, 'GeometryRepresentation')

# get 2D transfer function for 'alphaair'
alphaairTF2D = GetTransferFunction2D('alphaair')

# get color transfer function/color map for 'alphaair'
alphaairLUT = GetColorTransferFunction('alphaair')
alphaairLUT.TransferFunction2D = alphaairTF2D
alphaairLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour5Display.Representation = 'Surface'
contour5Display.ColorArrayName = ['POINTS', 'alpha.air']
contour5Display.DiffuseColor = [0.0, 0.0, 0.0]
contour5Display.LookupTable = alphaairLUT
contour5Display.SelectTCoordArray = 'None'
contour5Display.SelectNormalArray = 'Normals'
contour5Display.SelectTangentArray = 'None'
contour5Display.OSPRayScaleArray = 'alpha.air'
contour5Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour5Display.SelectOrientationVectors = 'U'
contour5Display.ScaleFactor = 1.7300539184361698e-06
contour5Display.SelectScaleArray = 'alpha.air'
contour5Display.GlyphType = 'Arrow'
contour5Display.GlyphTableIndexArray = 'alpha.air'
contour5Display.GaussianRadius = 8.650269592180848e-08
contour5Display.SetScaleArray = ['POINTS', 'alpha.air']
contour5Display.ScaleTransferFunction = 'PiecewiseFunction'
contour5Display.OpacityArray = ['POINTS', 'alpha.air']
contour5Display.OpacityTransferFunction = 'PiecewiseFunction'
contour5Display.DataAxesGrid = 'GridAxesRepresentation'
contour5Display.PolarAxes = 'PolarAxesRepresentation'
contour5Display.SelectInputVectors = ['POINTS', 'U']
contour5Display.ColorMode = 'Multiply'
contour5Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour5Display.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour5Display.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# hide data in view
Hide(transform3, renderView1)

# show color bar/color legend
contour5Display.SetScalarBarVisibility(renderView1, True)

# change representation type
contour5Display.SetRepresentationType('Points')

# set active source
SetActiveSource(transform3)

# show data in view
transform3Display = Show(transform3, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
transform3Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(fluidfoam)

# create a new 'Contour'
contour6 = Contour(registrationName='Contour6', Input=fluidfoam)
contour6.ContourBy = ['POINTS', 'p']
contour6.Isosurfaces = [545923174.5]
contour6.PointMergeMethod = 'Uniform Binning'

# show data in view
contour6Display = Show(contour6, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour6Display.Representation = 'Surface'
contour6Display.ColorArrayName = ['POINTS', 'alpha.air']
contour6Display.DiffuseColor = [0.0, 0.0, 0.0]
contour6Display.LookupTable = alphaairLUT
contour6Display.SelectTCoordArray = 'None'
contour6Display.SelectNormalArray = 'Normals'
contour6Display.SelectTangentArray = 'None'
contour6Display.OSPRayScaleArray = 'alpha.air'
contour6Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour6Display.SelectOrientationVectors = 'U'
contour6Display.ScaleFactor = 1.7300539184361698e-06
contour6Display.SelectScaleArray = 'alpha.air'
contour6Display.GlyphType = 'Arrow'
contour6Display.GlyphTableIndexArray = 'alpha.air'
contour6Display.GaussianRadius = 8.650269592180848e-08
contour6Display.SetScaleArray = ['POINTS', 'alpha.air']
contour6Display.ScaleTransferFunction = 'PiecewiseFunction'
contour6Display.OpacityArray = ['POINTS', 'alpha.air']
contour6Display.OpacityTransferFunction = 'PiecewiseFunction'
contour6Display.DataAxesGrid = 'GridAxesRepresentation'
contour6Display.PolarAxes = 'PolarAxesRepresentation'
contour6Display.SelectInputVectors = ['POINTS', 'U']
contour6Display.ColorMode = 'Multiply'
contour6Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour6Display.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour6Display.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# hide data in view
Hide(fluidfoam, renderView1)

# show color bar/color legend
contour6Display.SetScalarBarVisibility(renderView1, True)

# change representation type
contour6Display.SetRepresentationType('Points')

# set active source
SetActiveSource(fluidfoam)

# show data in view
fluidfoamDisplay = Show(fluidfoam, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
fluidfoamDisplay.SetScalarBarVisibility(renderView1, True)

# create a new 'Glyph'
glyph3 = Glyph(registrationName='Glyph3', Input=fluidfoam,
    GlyphType='Arrow')
glyph3.OrientationArray = ['POINTS', 'U']
glyph3.ScaleArray = ['POINTS', 'p']
glyph3.ScaleFactor = 0.0004999999888241291
glyph3.GlyphTransform = 'Transform2'

# show data in view
glyph3Display = Show(glyph3, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
glyph3Display.Representation = 'Surface'
glyph3Display.ColorArrayName = ['POINTS', 'p']
glyph3Display.DiffuseColor = [0.0, 0.0, 0.0]
glyph3Display.LookupTable = pLUT
glyph3Display.SelectTCoordArray = 'None'
glyph3Display.SelectNormalArray = 'None'
glyph3Display.SelectTangentArray = 'None'
glyph3Display.OSPRayScaleArray = 'p'
glyph3Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph3Display.SelectOrientationVectors = 'U'
glyph3Display.ScaleFactor = 0.0005020000040531159
glyph3Display.SelectScaleArray = 'p'
glyph3Display.GlyphType = 'Arrow'
glyph3Display.GlyphTableIndexArray = 'p'
glyph3Display.GaussianRadius = 2.5100000202655794e-05
glyph3Display.SetScaleArray = ['POINTS', 'p']
glyph3Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph3Display.OpacityArray = ['POINTS', 'p']
glyph3Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph3Display.DataAxesGrid = 'GridAxesRepresentation'
glyph3Display.PolarAxes = 'PolarAxesRepresentation'
glyph3Display.SelectInputVectors = ['POINTS', 'U']
glyph3Display.ColorMode = 'Multiply'
glyph3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph3Display.ScaleTransferFunction.Points = [101325.0, 0.0, 0.5, 0.0, 1003464000.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph3Display.OpacityTransferFunction.Points = [101325.0, 0.0, 0.5, 0.0, 1003464000.0, 1.0, 0.5, 0.0]

# show color bar/color legend
glyph3Display.SetScalarBarVisibility(renderView1, True)

# turn off scalar coloring
ColorBy(glyph3Display, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# set active source
SetActiveSource(contour6)

# hide color bar/color legend
contour6Display.SetScalarBarVisibility(renderView1, False)

# get opacity transfer function/opacity map for 'alphaair'
alphaairPWF = GetOpacityTransferFunction('alphaair')
alphaairPWF.ScalarRangeInitialized = 1
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# set active source
SetActiveSource(fluidfoam)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# get separate color transfer function/color map for 'U'
separate_fluidfoamDisplay_ULUT = GetColorTransferFunction('U', fluidfoamDisplay, separate=True)
separate_fluidfoamDisplay_ULUT.AutomaticRescaleRangeMode = 'Clamp and update every timestep'
separate_fluidfoamDisplay_ULUT.RescaleOnVisibilityChange = 1
separate_fluidfoamDisplay_ULUT.TransferFunction2D = uTF2D
separate_fluidfoamDisplay_ULUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 4.426662610399884, 0.865003, 0.865003, 0.865003, 8.853325220799768, 0.705882, 0.0156863, 0.14902]
separate_fluidfoamDisplay_ULUT.ScalarRangeInitialized = 1.0

# get separate opacity transfer function/opacity map for 'U'
separate_fluidfoamDisplay_UPWF = GetOpacityTransferFunction('U', fluidfoamDisplay, separate=True)
separate_fluidfoamDisplay_UPWF.Points = [0.0, 0.0, 0.5, 0.0, 8.853325220799768, 1.0, 0.5, 0.0]
separate_fluidfoamDisplay_UPWF.ScalarRangeInitialized = 1
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# Rescale transfer function
separate_fluidfoamDisplay_ULUT.RescaleTransferFunction(0.0, 1.1757813367477812e-38)

# Rescale transfer function
separate_fluidfoamDisplay_UPWF.RescaleTransferFunction(0.0, 1.1757813367477812e-38)

# get separate color transfer function/color map for 'p'
separate_transform3Display_pLUT = GetColorTransferFunction('p', transform3Display, separate=True)
separate_transform3Display_pLUT.AutomaticRescaleRangeMode = 'Clamp and update every timestep'
separate_transform3Display_pLUT.RescaleOnVisibilityChange = 1
separate_transform3Display_pLUT.TransferFunction2D = pTF2D
separate_transform3Display_pLUT.RGBPoints = [9410.677734375, 0.231373, 0.298039, 0.752941, 82964.0888671875, 0.865003, 0.865003, 0.865003, 156517.5, 0.705882, 0.0156863, 0.14902]
separate_transform3Display_pLUT.ScalarRangeInitialized = 1.0

# Rescale transfer function
separate_transform3Display_pLUT.RescaleTransferFunction(101325.0, 1091745024.0)

# get separate opacity transfer function/opacity map for 'p'
separate_transform3Display_pPWF = GetOpacityTransferFunction('p', transform3Display, separate=True)
separate_transform3Display_pPWF.Points = [9410.677734375, 0.0, 0.5, 0.0, 156517.5, 1.0, 0.5, 0.0]
separate_transform3Display_pPWF.ScalarRangeInitialized = 1

# Rescale transfer function
separate_transform3Display_pPWF.RescaleTransferFunction(101325.0, 1091745024.0)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

animationScene1.GoToFirst()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1612, 745)

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# save animation
SaveAnimation('/media/Hengzhu/DRIVE3:DATAH/solid/2.0/2.0.avi', renderView1, ImageResolution=[1612, 744],
    FrameRate=12,
    FrameWindow=[0, 100])
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1612, 745)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).