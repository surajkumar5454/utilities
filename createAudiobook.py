import PyPDF2
import pyttsx3

name = 'bigbook'
pdfName = name+'.pdf'
audioName = name+'.wmv'
pdfReader = PyPDF2.PdfFileReader(open(pdfName, 'rb'))
speaker = pyttsx3.init()
text = " "
for page_num in range(pdfReader.numPages):
    text2 = pdfReader.getPage(page_num).extractText()
    text += text2
    # speaker.say(text)
    print(page_num)
#    speaker.runAndWait()
# speaker.stop()
speaker.save_to_file(text, audioName)
speaker.runAndWait()
print("Finish")
