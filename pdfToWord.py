# Importing the Converter() class
import pdf2docx
# from pdf2docx import Converter
from tkinter import filedialog
from tkinter.ttk import *
import tkinter as tk

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
    local_files = filedialog.askopenfilename(filetypes=[("PDF/IMAGE", "*.pdf")])
    global file
    file = local_files
    if local_files != "":
        btn2["state"] = "enable"
    success_msg.set("")
    return


def download_file():
    local_savefile = filedialog.asksaveasfilename(defaultextension='.docx', filetypes=[("DOC", "*.docx")])
    global savefile
    savefile = local_savefile
    if local_savefile != "":
        btn3["state"] = "enable"
    return


def convert():
    success_msg.set("Please Wait...")
    root.update()
    cv_obj = pdf2docx.Converter(file)
    cv_obj.convert(savefile)
    cv_obj.close()
    success_msg.set("File Converted Successfully")
    btn2["state"] = "disabled"
    btn3["state"] = "disabled"
    print("File Converted Successfully")
    success_msg.set("File Converted Successfully")
    btn2["state"] = "disabled"
    btn3["state"] = "disabled"


root.mainloop()
