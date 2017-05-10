from core.main import data_file_names, image_file_names
from core.conversion import convert_pdf_to_image
from core.extraction import extract_data_from_image
from analysis import processLanguage

processLanguage()

for filename in data_file_names():
    convert_pdf_to_image(filename)

for filename in image_file_names():
    extract_data_from_image(filename)
