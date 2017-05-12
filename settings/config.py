# Settings and configurations here.
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Source file directories.
PDF_DIR = BASE_DIR + '/project_data/source_pdf_files/'
IMG_DIR = BASE_DIR + '/project_data/converted_images/'
TXT_DIR = BASE_DIR + '/project_data/extracted_text_files/'

# Conversion specific settings.
CONVERSION_RESOLUTION = '150'
