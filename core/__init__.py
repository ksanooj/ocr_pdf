import os

from core.utils import data_file_names, image_file_names, dir_names
from core.conversion import convert_pdf_to_image
from core.ocr import extract_data_from_image
from settings import IMG_DIR, PDF_DIR, TXT_DIR


def convert_files():

    for filename in data_file_names(PDF_DIR):
        img = convert_pdf_to_image(filename)
        img_dir = IMG_DIR + filename.split('/')[-1].split('.')[-2] + '/'
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)
        img_name = img_dir + 'page.jpg'
        img.save(filename=img_name)


def extract_business_names():

    for img_dir in dir_names(IMG_DIR):
        data = []
        for image in image_file_names(img_dir):
            data.append(extract_data_from_image(image))
        out_file = TXT_DIR + img_dir.split('/')[-1] + '.txt'
        with open(out_file, 'w') as out:
            out.write('\n'.join(data))
            # print('created ' + out_file)

convert_files()
extract_business_names()
