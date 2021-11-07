import SimpleITK as sitk

fixedImage = sitk.ReadImage('fixedImage.png')
movingImage = sitk.ReadImage('movingImage.png')
parameterMap = sitk.GetDefaultParameterMap('translation')

elastixImageFilter = sitk.ElastixImageFilter()
elastixImageFilter.SetFixedImage(fixedImage)
elastixImageFilter.SetMovingImage(movingImage)
elastixImageFilter.SetParameterMap(parameterMap)
elastixImageFilter.Execute()

resultImage = elastixImageFilter.GetResultImage()
transformParameterMap = elastixImageFilter.GetTransformParameterMap()

sitk.Show(resultImage, title="Hello World: Python", debugOn=True)