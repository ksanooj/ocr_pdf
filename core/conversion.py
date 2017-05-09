from wand.image import Image as WI
from settings import IMG_DIR


def convert_pdf_to_image(pdf):
    with WI(filename=pdf, resolution=140) as img:
        img_file = IMG_DIR + pdf.split('/')[-1].split('.')[-2] + '.jpg'
        img = img.convert('jpg')
        img.save(filename=img_file)

        print('created ' + img_file)

import PyPDF2
from PIL import Image


def convert_using_pypdf(pdf):
    input1 = PyPDF2.PdfFileReader(open(pdf, "rb"))
    page0 = input1.getPage(0)
    xObject = page0['/Resources']['/XObject'].getObject()

    for obj in xObject:
        if xObject[obj]['/Subtype'] == '/Image':
            size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
            data = xObject[obj].getData()
            if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                mode = "RGB"
            else:
                mode = "P"

            if xObject[obj]['/Filter'] == '/FlateDecode':
                img = Image.frombytes(mode, size, data)
                img.save(obj[1:] + ".png")
            elif xObject[obj]['/Filter'] == '/DCTDecode':
                img = open(obj[1:] + ".jpg", "wb")
                img.write(data)
                img.close()
            elif xObject[obj]['/Filter'] == '/JPXDecode':
                img = open(obj[1:] + ".jp2", "wb")
                img.write(data)
                img.close()

