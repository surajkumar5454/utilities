import shutil
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time

import tkinter as tk
import tkinter.filedialog as filedg

import pytesseract
from pdf2image import convert_from_path

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

root = tk.Tk()
root.geometry("400x200")

lbl = Label(text="Upload file")
lbl.grid(row=1, column=3)
btn = Button(text="Upload", command=lambda: upload_file())
btn.grid(row=1, column=4)
lbl2 = Label(text="Path to save file")
lbl2.grid(row=2, column=3)
btn2 = Button(text="Download", command=lambda: download_file())
btn2.grid(row=2, column=4)

success_msg = tk.StringVar()
lbl3 = Label(textvariable=success_msg)
lbl3.grid(row=4, column=3)
success_msg.set("")


def upload_file():
    file = filedialog.askopenfilename(filetypes=[("PDF", "*.pdf"), ("Image", "*.jpeg"), ("All Files", "*.*")])
    if file.endswith('.pdf'):
        path_to_image = convert_from_path(file, poppler_path=r"C:\Program Files\poppler\Library\bin")
        ocr_text = pytesseract.image_to_string(path_to_image[0])
        PDF = pytesseract.image_to_pdf_or_hocr(path_to_image[0], extension='pdf')
    elif file.endswith('.jpeg'):
        PDF = pytesseract.image_to_pdf_or_hocr(file, extension='pdf')
    with open("searchable.pdf", "w+b") as f:
        f.write(bytearray(PDF))


def download_file():
    savefile = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[("PDF", "*.pdf")])
    shutil.move('searchable.pdf', savefile)
    success_msg.set("File Converted Successfully")


root.mainloop()
