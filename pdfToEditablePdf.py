import pytesseract
from pdf2image import convert_from_path

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# path_to_image = 'hraimagefile.jpeg'
pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

# convert PDF to image
# images = convert_from_path('imagepdf.pdf', poppler_path=poppler_path)
path_to_image = convert_from_path('imagepdf.pdf', poppler_path=r"C:\Program Files\poppler\Library\bin")
# Extract text from image
ocr_text = pytesseract.image_to_string(path_to_image[0])

# Handle Multiple Pages in PDF
# If there are multiple pages in a PDF, we can simply use a loop function to combine text from all the pages.


# images = convert_from_path('example.pdf', poppler_path=poppler_path)
# ocr_text = ''
# for i in range(len(images)):
#     page_content = pytesseract.image_to_string(images[i])
#     page_content = '***PDF Page {}***\n'.format(i+1) + page_content
#     ocr_text = ocr_text + ' ' + page_content


PDF = pytesseract.image_to_pdf_or_hocr(path_to_image[0], extension='pdf')
# export to searchable.pdf
with open("searchable.pdf", "w+b") as f:
    f.write(bytearray(PDF))

# https://towardsdatascience.com/pdf-text-extraction-while-preserving-whitespaces-using-python-and-pytesseract-ec142743e805
