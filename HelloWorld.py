import SimpleITK as sitk

fixed = sitk.ReadImage("HE_PHH3/Bio5_HE.png", sitk.sitkUInt8)
moving = sitk.ReadImage("HE_PHH3/Bio5_PHH3.png", sitk.sitkUInt8)

resultImage = sitk.Elastix(fixed, moving, "translation")
resultImage = sitk.Cast(resultImage, sitk.sitkUInt8)

sitk.WriteImage(resultImage, "resultImage.png")
