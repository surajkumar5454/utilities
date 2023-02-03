import PyPDF2
from gtts import gTTS
from tkinter import filedialog
from tkinter.ttk import *
import tkinter as tk


root = tk.Tk()
root.geometry("400x200")

lbl = Label(text="Enter Source File (*.txt,*.pdf)")
lbl.grid(row=1, column=3)
btn = Button(text="Upload", command=lambda: upload_file())
btn.grid(row=1, column=4)
lbl2 = Label(text="Audiobook")
lbl2.grid(row=2, column=3)
btn2 = Button(text="Save file as ", command=lambda: download_file())
btn2.grid(row=2, column=4)

btn3 = Button(text="CONVERT", command=lambda: convert())
btn3.grid(row=3, column=4)
btn2["state"]= "disabled"
btn3["state"]= "disabled"
success_msg = tk.StringVar()
lbl3 = tk.Label(textvariable=success_msg, fg='green')
lbl3.grid(row=4, column=3)
success_msg.set("")

def upload_file():
    filename = filedialog.askopenfilename(filetypes=[("PDF/TXT", "*.pdf"), ("PDF/TXT", "*.txt")])
    global file
    file = filename
    if filename!="":
        btn2["state"] = "enable"
    return


def download_file():
    savefilename = filedialog.asksaveasfilename(defaultextension='.wav', filetypes=[("Audio", "*.wav")])
    global savefile
    savefile = savefilename
    if savefilename != "":
        btn3["state"] = "enable"
    return


def convert():
    mytext = " "
    if file.endswith('.pdf'):
        pdfReader = PyPDF2.PdfFileReader(open(file, 'rb'))
        for page_num in range(pdfReader.numPages):
            text2 = pdfReader.getPage(page_num).extractText()
            mytext += text2
    elif file.endswith('.txt'):
        mytext = open(file, 'r', encoding='utf-8').read() \
            .replace('\n\n', '*newline*') \
            .replace('\n', ' ') \
            .replace('*newline*', '\n\n')

    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    outputfile = savefile
    myobj.save(outputfile)
    success_msg.set("File Converted Successfully")
    btn2["state"] = "disabled"
    btn3["state"] = "disabled"

root.mainloop()