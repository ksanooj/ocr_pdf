from wand.image import Image as WI
from setup import IMG_DIR
# import cv2


def convert_pdf_to_image(pdf):
    with WI(filename=pdf) as img:
        img_file = IMG_DIR + pdf.split('/')[-1].split('.')[-2] + '.jpg'
        img = img.convert('jpg')
        # image = cv2.imread(img)
        img.save(filename=img_file)
        print('created ' + img_file)
