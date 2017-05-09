from tesserocr import PytessBaseAPI
from core import image_file_names


with PytessBaseAPI() as api:
    for img in image_file_names():
        api.SetImageFile(img)
        print(api.GetUTF8Text())
        print(api.AllWordConfidences())
