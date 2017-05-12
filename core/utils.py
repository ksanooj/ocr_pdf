import os


def data_file_names(pdf_dir):
    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            yield pdf_dir + filename
        else:
            continue


def image_file_names(img_dir):
    for filename in os.listdir(img_dir):
        if filename.endswith(".jpg"):
            yield img_dir + '/' + filename
        else:
            continue


def text_file_names(txt_dir):
    for filename in os.listdir(txt_dir):
        if filename.endswith(".txt"):
            yield txt_dir + filename
        else:
            continue


def dir_names(source_dir):
    for directory in os.listdir(source_dir):
        if os.path.isdir(source_dir + directory):
            yield source_dir + directory
        else:
            continue
