from tkinter import filedialog
from tkinter.ttk import *
import tkinter as tk
import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfMerger
from PyPDF2 import PdfFileReader, PdfFileWriter
from fpdf import FPDF

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

btn3 = Button(text="CONVERT", command=lambda: convert())
btn3.grid(row=3, column=4)

btn2["state"] = "disabled"
btn3["state"] = "disabled"

success_msg = tk.StringVar()
lbl3 = tk.Label(textvariable=success_msg, fg="green")
lbl3.grid(row=4, column=3)
success_msg.set("")



def upload_file():
    local_files = filedialog.askopenfilename(filetypes=[("PDF/IMAGE", "*.pdf"),("PDF/IMAGE", "*.jpeg")])
    global file
    file = local_files
    if local_files!="":
        btn2["state"] = "enable"
    success_msg.set("")
    return


def download_file():
    local_savefile = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[("PDF", "*.pdf")])
    global savefile
    savefile = local_savefile
    if local_savefile != "":
        btn3["state"] = "enable"
    return

def convert():
    if file.endswith('.pdf'):
        path_to_image = convert_from_path(file, poppler_path=r"C:\Program Files\poppler\Library\bin")
        ocr_text = pytesseract.image_to_string(path_to_image[0])
        writer = PdfFileWriter()
        for i in range(len(path_to_image)):
            PDF = pytesseract.image_to_pdf_or_hocr(path_to_image[i], extension='pdf')
            with open(savefile, "w+b") as f:
                f.write(bytearray(PDF))
            temp_pdf = PdfFileReader(savefile)                  # logic for multiple pages PDF
            writer.addPage(temp_pdf.getPage(0))
        writer.write(savefile)
    elif file.endswith('.jpeg'):
        PDF = pytesseract.image_to_pdf_or_hocr(file, extension='pdf')
        with open(savefile, "w+b") as f:
            f.write(bytearray(PDF))
    success_msg.set("File Converted Successfully")
    btn2["state"] = "disabled"
    btn3["state"] = "disabled"
    print("File Converted Successfully")

root.mainloop()
