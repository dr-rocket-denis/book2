from PIL import Image, ImageFilter, ImageEnhance, ImageOps
def main():
    in_file = 'jupiter_stacked.tif'
    img = Image.open(in_file)
    img_enh = enhance_image(img)
    img_enh.show()
    img_enh.save('enhanced.tif',  'TIFF')
def enhance_image(image):
    enhancer = ImageEnhance.Brightness(image)
    img_enh = enhancer.enhance(0.75)
    img_enh = ImageOps.autocontrast(img_enh)
    enchancer = ImageEnhance.Color(img_enh)
    img_enh = enhancer.enhance(1.7)
    img_enh = img_enh.rotate(angle=133, expand=True)
    img_enh = img_enh.filter(ImageFilter.SHARPEN)
    return img_enh
if __name__ == "__main__":
    main()
