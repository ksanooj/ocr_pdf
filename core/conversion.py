# utilities to convert pdf to image
import os
from wand.image import Image as WI


def convert_pdf_to_image(pdf):
    with WI(filename=pdf, resolution=int(os.environ['CONVERSION_RESOLUTION'])) as img:
        img.compression_quality = 99
        return img.convert('jpeg')


def convert_pdf_to_image_blob(pdf):
    image_jpeg = convert_pdf_to_image(pdf=pdf)
    req_image = []
    for img in image_jpeg.sequence:
        img_page = WI(image=img)
        req_image.append(img_page.make_blob('jpeg'))
    return req_image
