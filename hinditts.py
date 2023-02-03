import PyPDF2
from gtts import gTTS
import os

filename = input("Enter Hindi source file name (including extension):     ")

x = filename.split(".")
filenamestring = x[0]
extension = x[1]

if extension != "pdf":
    # clean up a bit on the text to remove newlines, but not remove paragraph lines
    mytext = open(filename, 'r', encoding='utf-8').read() \
        .replace('\n\n', '*newline*') \
        .replace('\n', ' ') \
        .replace('*newline*', '\n\n')

else:
    pdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))
    mytext = " "
    for page_num in range(pdfReader.numPages):
        text2 = pdfReader.getPage(page_num).extractText()
        mytext += text2

# Language in which you want to convert
language = 'hi'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
outputfile = filenamestring + ".wav"
myobj.save(outputfile)

# Playing the converted file
os.system(outputfile)
