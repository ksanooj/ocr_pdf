#!/usr/bin/env python
import os
import sys
import settings

if __name__ == "__main__":

    os.environ['BASE_DIR'] = settings.BASE_DIR or os.path.dirname(__file__)
    os.environ['PDF_DIR'] = settings.PDF_DIR or (os.path.dirname(__file__) + '/project_data/source_pdf_files/')
    os.environ['IMG_DIR'] = settings.IMG_DIR or (os.path.dirname(__file__) + '/project_data/converted_images/')
    os.environ['TXT_DIR'] = settings.TXT_DIR or (os.path.dirname(__file__) + '/project_data/extracted_text_files/')
    os.environ['CONVERSION_RESOLUTION'] = settings.CONVERSION_RESOLUTION or '160'

    if "execute" in sys.argv:
        execfile(os.path.abspath(os.path.dirname(__file__)) + '/core/__init__.py')

    if "convert" in sys.argv:
        from core import convert_files
        convert_files()
    if "extract" in sys.argv:
        from core import extract_business_names
        extract_business_names()
