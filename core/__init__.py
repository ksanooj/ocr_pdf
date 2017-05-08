from main import data_file_names, convert_pdf_to_image, image_file_names

for filename in data_file_names():
    convert_pdf_to_image(filename)
