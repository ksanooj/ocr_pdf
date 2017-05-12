from PIL import Image, ImageFilter
import pytesseract


def extract_data_from_image(fp):

    image = Image.open(fp)

    image = image.filter(ImageFilter.SHARPEN)

    text = pytesseract.image_to_string(image=image, lang='eng')
    return text
