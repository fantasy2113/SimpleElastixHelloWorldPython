import SimpleITK as sitk

resultImage = sitk.Elastix(sitk.ReadImage("sae/he_phh3/Bio5_HE.png", sitk.sitkInt8),
                           sitk.ReadImage("sae/he_phh3/Bio5_PHH3.png", sitk.sitkInt8), "translation")

sitk.Show(resultImage, title="Hello World: Python", debugOn=True)