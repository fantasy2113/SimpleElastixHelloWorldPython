import SimpleITK as sitk

resultImage = sitk.Elastix(sitk.ReadImage("fixedImage.png"),sitk.ReadImage("movingImage.png"), "translation")

sitk.Show(resultImage, title="Hello World: Python", debugOn=True)