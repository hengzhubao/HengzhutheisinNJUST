# trace generated using paraview version 5.11.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
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

# get 2D transfer function for 'alphaair'
alphaairTF2D = GetTransferFunction2D('alphaair')

# get color transfer function/color map for 'alphaair'
alphaairLUT = GetColorTransferFunction('alphaair')
alphaairLUT.TransferFunction2D = alphaairTF2D
alphaairLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for alphaairLUT in view renderView1
alphaairLUTColorBar = GetScalarBar(alphaairLUT, renderView1)
alphaairLUTColorBar.WindowLocation = 'Upper Left Corner'
alphaairLUTColorBar.Position = [0.0024813895781637717, 0.6536912751677852]
alphaairLUTColorBar.Title = 'alpha.air'
alphaairLUTColorBar.ComponentTitle = ''
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

# find source
contour6 = FindSource('Contour6')

# set active source
SetActiveSource(contour6)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# get opacity transfer function/opacity map for 'alphaair'
alphaairPWF = GetOpacityTransferFunction('alphaair')
alphaairPWF.ScalarRangeInitialized = 1

# get display properties
contour6Display = GetDisplayProperties(contour6, view=renderView1)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# hide color bar/color legend
contour6Display.SetScalarBarVisibility(renderView1, False)
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

# find source
fluidfoam = FindSource('fluid.foam')

# get display properties
fluidfoamDisplay = GetDisplayProperties(fluidfoam, view=renderView1)

# get 2D transfer function for 'U'
uTF2D = GetTransferFunction2D('U')

# get separate color transfer function/color map for 'U'
separate_fluidfoamDisplay_ULUT = GetColorTransferFunction('U', fluidfoamDisplay, separate=True)
separate_fluidfoamDisplay_ULUT.AutomaticRescaleRangeMode = 'Clamp and update every timestep'
separate_fluidfoamDisplay_ULUT.RescaleOnVisibilityChange = 1
separate_fluidfoamDisplay_ULUT.TransferFunction2D = uTF2D
separate_fluidfoamDisplay_ULUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 4.426662610399884, 0.865003, 0.865003, 0.865003, 8.853325220799768, 0.705882, 0.0156863, 0.14902]
separate_fluidfoamDisplay_ULUT.ScalarRangeInitialized = 1.0

# get color legend/bar for separate_fluidfoamDisplay_ULUT in view renderView1
separate_fluidfoamDisplay_ULUTColorBar = GetScalarBar(separate_fluidfoamDisplay_ULUT, renderView1)
separate_fluidfoamDisplay_ULUTColorBar.Title = 'U'
separate_fluidfoamDisplay_ULUTColorBar.ComponentTitle = 'Magnitude'

# change scalar bar placement
separate_fluidfoamDisplay_ULUTColorBar.Position = [0.9280397022332506, 0.016107382550335572]
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# change scalar bar placement
separate_fluidfoamDisplay_ULUTColorBar.Orientation = 'Vertical'
separate_fluidfoamDisplay_ULUTColorBar.WindowLocation = 'Any Location'
separate_fluidfoamDisplay_ULUTColorBar.Position = [0.9212158808933001, 0.1798657718120805]
separate_fluidfoamDisplay_ULUTColorBar.ScalarBarLength = 0.3300000000000004
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

# change scalar bar placement
separate_fluidfoamDisplay_ULUTColorBar.Position = [0.8337468982630272, 0.002684563758389255]
separate_fluidfoamDisplay_ULUTColorBar.ScalarBarLength = 0.33000000000000057
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

# change scalar bar placement
separate_fluidfoamDisplay_ULUTColorBar.Position = [0.7351116625310172, 0.0]
separate_fluidfoamDisplay_ULUTColorBar.ScalarBarLength = 0.3300000000000006
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# change scalar bar placement
separate_fluidfoamDisplay_ULUTColorBar.Orientation = 'Horizontal'
separate_fluidfoamDisplay_ULUTColorBar.Position = [0.32012406947890754, 0.1497986577181211]
separate_fluidfoamDisplay_ULUTColorBar.ScalarBarLength = 0.3300000000000008
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

# change scalar bar placement
separate_fluidfoamDisplay_ULUTColorBar.Position = [0.6036228287841184, 0.012885906040268735]
separate_fluidfoamDisplay_ULUTColorBar.ScalarBarLength = 0.33000000000000085
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

# find source
transform3 = FindSource('Transform3')

# get display properties
transform3Display = GetDisplayProperties(transform3, view=renderView1)

# get 2D transfer function for 'p'
pTF2D = GetTransferFunction2D('p')

# get separate color transfer function/color map for 'p'
separate_transform3Display_pLUT = GetColorTransferFunction('p', transform3Display, separate=True)
separate_transform3Display_pLUT.AutomaticRescaleRangeMode = 'Clamp and update every timestep'
separate_transform3Display_pLUT.RescaleOnVisibilityChange = 1
separate_transform3Display_pLUT.TransferFunction2D = pTF2D
separate_transform3Display_pLUT.RGBPoints = [9410.677734375, 0.231373, 0.298039, 0.752941, 82964.0888671875, 0.865003, 0.865003, 0.865003, 156517.5, 0.705882, 0.0156863, 0.14902]
separate_transform3Display_pLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for separate_transform3Display_pLUT in view renderView1
separate_transform3Display_pLUTColorBar = GetScalarBar(separate_transform3Display_pLUT, renderView1)
separate_transform3Display_pLUTColorBar.WindowLocation = 'Upper Right Corner'
separate_transform3Display_pLUTColorBar.Title = 'p'
separate_transform3Display_pLUTColorBar.ComponentTitle = ''

# change scalar bar placement
separate_transform3Display_pLUTColorBar.Position = [0.9280397022332506, 0.6536912751677852]
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [1.4689040637675394e-05, 0.0005199340643155786, 0.002456941915223783]
renderView1.CameraFocalPoint = [1.4689040637675394e-05, 0.0005199340643155786, 0.0]
renderView1.CameraParallelScale = 0.0035355701030322885

# change scalar bar placement
separate_transform3Display_pLUTColorBar.Orientation = 'Horizontal'
separate_transform3Display_pLUTColorBar.WindowLocation = 'Any Location'
separate_transform3Display_pLUTColorBar.Position = [0.07880893300248118, 0.0026845637583892616]
separate_transform3Display_pLUTColorBar.ScalarBarLength = 0.3300000000000002
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