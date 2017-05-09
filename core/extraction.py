from settings import TXT_DIR
from PIL import Image
import pytesseract
# import os


def extract_data_from_image(fp):
    text = pytesseract.image_to_string(image=Image.open(fp), lang='eng')
    out_file = TXT_DIR + fp.split('/')[-1].split('.')[-2] + '.txt'
    with open(out_file, 'w') as out:
        out.write(text)
        print('created ' + fp.split('/')[-1].split('.')[-2] + '.txt')
    # os.remove(fp)
