from settings import PDF_DIR, IMG_DIR, TXT_DIR
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


def text_file_names():
    for filename in os.listdir(TXT_DIR):
        if filename.endswith(".txt"):
            yield TXT_DIR + filename
        else:
            continue
