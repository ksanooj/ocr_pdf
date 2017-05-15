import os

from core.utils import data_file_names, image_file_names, dir_names
from core.conversion import convert_pdf_to_image, convert_pdf_to_image_blob
from core.ocr import extract_data_from_image, extract_data_from_blob
from core.entity_recognition import process_with_stanford_ner
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


def extract_business_name_from_pdf_using_pyocr():

    for filename in data_file_names(PDF_DIR):
        blob_list = convert_pdf_to_image_blob(filename)
        data_list = extract_data_from_blob(blob_list)
        business_names = process_with_stanford_ner(data_list)
        print business_names

# convert_files()
# extract_business_names()
extract_business_name_from_pdf_using_pyocr()
