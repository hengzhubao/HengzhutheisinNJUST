# trace generated using paraview version 5.11.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
fluidfoam = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
fluidfoamDisplay = GetDisplayProperties(fluidfoam, view=renderView1)

# set scalar coloring
ColorBy(fluidfoamDisplay, ('POINTS', 'U', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
fluidfoamDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fluidfoamDisplay.SetScalarBarVisibility(renderView1, True)

# get 2D transfer function for 'U'
uTF2D = GetTransferFunction2D('U')

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')
uLUT.TransferFunction2D = uTF2D
uLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 48.04509050868726, 0.865003, 0.865003, 0.865003, 96.09018101737452, 0.705882, 0.0156863, 0.14902]
uLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')
uPWF.Points = [0.0, 0.0, 0.5, 0.0, 96.09018101737452, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# create a new 'Transform'
transform3 = Transform(registrationName='Transform3', Input=fluidfoam)
transform3.Transform = 'Transform'
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

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=transform3.Transform)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# find source
a01 = FindSource('0.1')

# find source
a20 = FindSource('2.0')

# find source
transform1 = FindSource('Transform1')

# find source
contour4 = FindSource('Contour4')

# Properties modified on fluidfoam
fluidfoam.CellArrays = ['T', 'T.air', 'T.oil', 'T.water', 'U', 'alpha.air', 'alpha.oil', 'alpha.water', 'alphas', 'dgdt.air', 'dgdt.oil', 'dgdt.water', 'inkMap', 'kinematicCloud:UCoeff', 'kinematicCloud:UTrans', 'p', 'p_rgh', 'rho_air', 'rho_oil', 'rho_water']

# find source
glyph1 = FindSource('Glyph1')

# find source
contour1 = FindSource('Contour1')

# find source
contour2 = FindSource('Contour2')

# find source
transform2 = FindSource('Transform2')

# find source
glyph2 = FindSource('Glyph2')

# find source
contour3 = FindSource('Contour3')

# Properties modified on transform3.Transform
transform3.Transform.Rotate = [0.0, 180.0, 0.0]

# show data in view
transform3Display = Show(transform3, renderView1, 'UnstructuredGridRepresentation')

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
transform3Display.ScalarOpacityUnitDistance = 8.583896581949656e-05
transform3Display.OpacityArrayName = ['POINTS', 'p']
transform3Display.SelectInputVectors = ['POINTS', 'U']
transform3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform3Display.ScaleTransferFunction.Points = [9410.677734375, 0.0, 0.5, 0.0, 156517.5, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform3Display.OpacityTransferFunction.Points = [9410.677734375, 0.0, 0.5, 0.0, 156517.5, 1.0, 0.5, 0.0]

# hide data in view
Hide(fluidfoam, renderView1)

# show color bar/color legend
transform3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()
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

# show data in view
fluidfoamDisplay = Show(fluidfoam, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
fluidfoamDisplay.SetScalarBarVisibility(renderView1, True)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# set scalar coloring using an separate color/opacity maps
ColorBy(fluidfoamDisplay, ('POINTS', 'U', 'Magnitude'), True)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(uLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
fluidfoamDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fluidfoamDisplay.SetScalarBarVisibility(renderView1, True)

# get separate 2D transfer function for 'U'
separate_fluidfoamDisplay_UTF2D = GetTransferFunction2D('U', fluidfoamDisplay, separate=True)

# get separate color transfer function/color map for 'U'
separate_fluidfoamDisplay_ULUT = GetColorTransferFunction('U', fluidfoamDisplay, separate=True)
separate_fluidfoamDisplay_ULUT.TransferFunction2D = separate_fluidfoamDisplay_UTF2D
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

# Properties modified on separate_fluidfoamDisplay_ULUT
separate_fluidfoamDisplay_ULUT.AutomaticRescaleRangeMode = 'Clamp and update every timestep'
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# Properties modified on separate_fluidfoamDisplay_ULUT
separate_fluidfoamDisplay_ULUT.RescaleOnVisibilityChange = 1
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

# set active source
SetActiveSource(transform3)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# set scalar coloring using an separate color/opacity maps
ColorBy(transform3Display, ('POINTS', 'p'), True)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
transform3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
transform3Display.SetScalarBarVisibility(renderView1, True)

# get separate 2D transfer function for 'p'
separate_transform3Display_pTF2D = GetTransferFunction2D('p', transform3Display, separate=True)

# get separate color transfer function/color map for 'p'
separate_transform3Display_pLUT = GetColorTransferFunction('p', transform3Display, separate=True)
separate_transform3Display_pLUT.TransferFunction2D = separate_transform3Display_pTF2D
separate_transform3Display_pLUT.RGBPoints = [9410.677734375, 0.231373, 0.298039, 0.752941, 82964.0888671875, 0.865003, 0.865003, 0.865003, 156517.5, 0.705882, 0.0156863, 0.14902]
separate_transform3Display_pLUT.ScalarRangeInitialized = 1.0

# get separate opacity transfer function/opacity map for 'p'
separate_transform3Display_pPWF = GetOpacityTransferFunction('p', transform3Display, separate=True)
separate_transform3Display_pPWF.Points = [9410.677734375, 0.0, 0.5, 0.0, 156517.5, 1.0, 0.5, 0.0]
separate_transform3Display_pPWF.ScalarRangeInitialized = 1
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

# Properties modified on separate_transform3Display_pLUT
separate_transform3Display_pLUT.AutomaticRescaleRangeMode = 'Clamp and update every timestep'
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# Properties modified on separate_transform3Display_pLUT
separate_transform3Display_pLUT.RescaleOnVisibilityChange = 1
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

# create a new 'Contour'
contour5 = Contour(registrationName='Contour5', Input=transform3)
contour5.ContourBy = ['POINTS', 'p']
contour5.Isosurfaces = [82964.0888671875]
contour5.PointMergeMethod = 'Uniform Binning'
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# Properties modified on contour5
contour5.ContourBy = ['POINTS', 'alpha.air']
contour5.Isosurfaces = [0.5]

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
contour5Display.ScaleFactor = 4.454474401427433e-05
contour5Display.SelectScaleArray = 'alpha.air'
contour5Display.GlyphType = 'Arrow'
contour5Display.GlyphTableIndexArray = 'alpha.air'
contour5Display.GaussianRadius = 2.2272372007137166e-06
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

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# get opacity transfer function/opacity map for 'alphaair'
alphaairPWF = GetOpacityTransferFunction('alphaair')
alphaairPWF.ScalarRangeInitialized = 1
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# change representation type
contour5Display.SetRepresentationType('Points')
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# set active source
SetActiveSource(transform3)

# show data in view
transform3Display = Show(transform3, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
transform3Display.SetScalarBarVisibility(renderView1, True)
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

# create a new 'Contour'
contour6 = Contour(registrationName='Contour6', Input=fluidfoam)
contour6.ContourBy = ['POINTS', 'p']
contour6.Isosurfaces = [82964.0888671875]
contour6.PointMergeMethod = 'Uniform Binning'

# Properties modified on contour6
contour6.ContourBy = ['POINTS', 'alpha.air']
contour6.Isosurfaces = [0.5]

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
contour6Display.ScaleFactor = 4.454474401427433e-05
contour6Display.SelectScaleArray = 'alpha.air'
contour6Display.GlyphType = 'Arrow'
contour6Display.GlyphTableIndexArray = 'alpha.air'
contour6Display.GaussianRadius = 2.2272372007137166e-06
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

# update the view to ensure updated data information
renderView1.Update()
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

# change representation type
contour6Display.SetRepresentationType('Points')
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# set active source
SetActiveSource(fluidfoam)

# show data in view
fluidfoamDisplay = Show(fluidfoam, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
fluidfoamDisplay.SetScalarBarVisibility(renderView1, True)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# create a new 'Glyph'
glyph3 = Glyph(registrationName='Glyph3', Input=fluidfoam,
    GlyphType='Arrow')
glyph3.OrientationArray = ['POINTS', 'U']
glyph3.ScaleArray = ['POINTS', 'p']
glyph3.ScaleFactor = 0.0004999999888241291
glyph3.GlyphTransform = 'Transform2'

# Properties modified on glyph3
glyph3.ScaleArray = ['POINTS', 'No scale array']
glyph3.ScaleFactor = 2e-05
glyph3.MaximumNumberOfSamplePoints = 100000
glyph3.Seed = 100000

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
glyph3Display.ScaleFactor = 0.0005024829794820107
glyph3Display.SelectScaleArray = 'p'
glyph3Display.GlyphType = 'Arrow'
glyph3Display.GlyphTableIndexArray = 'p'
glyph3Display.GaussianRadius = 2.5124148974100537e-05
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
glyph3Display.ScaleTransferFunction.Points = [9536.220703125, 0.0, 0.5, 0.0, 156517.5, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph3Display.OpacityTransferFunction.Points = [9536.220703125, 0.0, 0.5, 0.0, 156517.5, 1.0, 0.5, 0.0]

# show color bar/color legend
glyph3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()
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

# turn off scalar coloring
ColorBy(glyph3Display, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# change solid color
glyph3Display.AmbientColor = [0.1843137254901961, 0.1843137254901961, 0.1843137254901961]
glyph3Display.DiffuseColor = [0.1843137254901961, 0.1843137254901961, 0.1843137254901961]
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

# get layout
layout1 = GetLayout()

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