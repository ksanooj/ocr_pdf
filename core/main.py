from wand.image import Image as WI
from setup import PDF_DIR, IMG_DIR
import os


def data_file_names():
    for filename in os.listdir(PDF_DIR):
        if filename.endswith(".pdf"):
            yield PDF_DIR + filename
        else:
            continue


def image_file_names():
    for filename in os.listdir(IMG_DIR):
        if filename.endswith(".jpg"):
            yield IMG_DIR + filename
        else:
            continue


def convert_pdf_to_image(pdf):
    with WI(filename=pdf) as img:
        file_name = IMG_DIR + pdf.split('/')[-1].split('.')[-2] + '.jpg'
        img.convert('jpg').save(filename=file_name)
        print()
