from PIL import Image, ImageFilter
import pytesseract
import io
import pyocr
import pyocr.builders


def extract_data_from_image(fp):
    """
    Uses pytesseract to extract text from image files. Takes location string of an image as argument.
    Returns a string.
    """
    image = Image.open(fp)
    image = image.filter(ImageFilter.SHARPEN)
    text = pytesseract.image_to_string(image=image, lang='eng')
    return text


def extract_data_from_blob(blob_list):
    """
    Uses pyocr to extract text from image blobs. Takes a list of image blobs as argument.
    Returns a list of strings.
    """
    tool = pyocr.get_available_tools()[0]
    lang = tool.get_available_languages()[1]

    final_text = []
    for blob in blob_list:
        txt = tool.image_to_string(
            Image.open(io.BytesIO(blob)),
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )
        final_text.append(txt)
    return final_text
