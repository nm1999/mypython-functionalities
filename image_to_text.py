import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd = r'C:\Users\HON. NYANZI MATIA\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

img = Image.open('paint.png')
text = tess.image_to_string(img)
# text = tess.image_to_boxes(img)
# text = tess.image_to_pdf_or_hocr(img)
print(text)