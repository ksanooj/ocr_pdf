from core import image_file_names
from PIL import Image
import pytesseract


for f in image_file_names():
    text = pytesseract.image_to_string(image=Image.open(f))
    print(text)
