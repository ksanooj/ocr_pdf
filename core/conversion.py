from wand.image import Image as WI
from settings import IMG_DIR


def convert_pdf_to_image(pdf):
    with WI(filename=pdf, resolution=300) as img:
        img_file = IMG_DIR + pdf.split('/')[-1].split('.')[-2] + '.jpg'
        img = img.convert('jpg')
        img.save(filename=img_file)
