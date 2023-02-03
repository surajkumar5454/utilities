import pytesseract
from pdf2image import convert_from_path

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
path_to_image = 'hraimagefile.jpeg'
pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

PDF = pytesseract.image_to_pdf_or_hocr(path_to_image, extension='pdf')
# export to searchable.pdf
with open("imgToPdf.pdf", "w+b") as f:
    f.write(bytearray(PDF))

# https://towardsdatascience.com/pdf-text-extraction-while-preserving-whitespaces-using-python-and-pytesseract-ec142743e805
