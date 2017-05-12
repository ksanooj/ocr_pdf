# utilities to convert pdf to image
import os
from wand.image import Image as WI


def convert_pdf_to_image(pdf):
    with WI(filename=pdf, resolution=int(os.environ['CONVERSION_RESOLUTION'])) as img:
        img.compression_quality = 99
        return img.convert('jpg')
