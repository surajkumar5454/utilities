import PyPDF2
import requests
from flask import Flask, request, redirect, render_template
import os
import shutil
from gtts import gTTS
from werkzeug.utils import secure_filename

app = Flask(__name__)

filename = ""
r = requests.get('https://reqbin.com/echo', timeout=3600)
print(f"Status Code: {r.status_code}")


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template("index.html")


@app.route('/getfile', methods=['GET', 'POST'])
def getfile():
    if request.method == 'POST':
        # for secure filenames. Read the documentation.
        files = request.files['file']
        filename = secure_filename(files.filename)
        currentWorkingDirectory = os.getcwd()

        # os.path.join is used so that paths work in every operating system
        files.save(os.path.join( filename))
        #
        # # You should use os.path.join here too.
        # with open(currentWorkingDirectory+"\\"+filename) as f:
        #     file_content = f.read()
        #
        # return file_content
        print("inside get file")
        return redirect("/convert/" + filename)
    return "Error Page"


@app.route('/convert/<string:filename>', methods=['GET', 'POST'])
def convert(filename):
    print(filename)
    x = filename.split(".")
    filenamestring = x[0]
    extension = x[1]
    currentWorkingDirectory = os.getcwd()
    if extension != "pdf":
        # clean up a bit on the text to remove newlines, but not remove paragraph lines
        mytext = open(filename, 'r', encoding='utf-8').read() \
            .replace('\n\n', '*newline*') \
            .replace('\n', ' ') \
            .replace('*newline*', '\n\n')
    else:
        f = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(f)
        mytext = " "
        for page_num in range(pdfReader.numPages):
            text2 = pdfReader.getPage(page_num).extractText()
            mytext += text2
        f.close()
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filenamestring + ".mp3")
    #   os.system(outputfile)
    print("End of program")
    shutil.move(filenamestring+".mp3", "static/"+filenamestring+".mp3")

#   return redirect("/download/" + filenamestring)
    return "Your file is ready for download. Click <a href='/static/" + filenamestring + ".mp3'>here</a> to download<br> <a href='/'>HOME</a>"


# @app.route('/download/<string:filenamestring>', methods=['GET', 'POST'])
# def download(filenamestring):
#     return "Your file is ready for download. Click <a href='././" + filenamestring + ".mp3'>here</a> to download<br> <a href='/'>HOME</a>"


if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
