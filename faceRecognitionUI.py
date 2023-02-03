import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import *

import face_recognition

root = tk.Tk()  # create CTk window like you do with the Tk window
root.geometry("700x350")

app = Frame(root)
app.place(x=10, y=10)

blank_lbl = Label(app, text="SASHASTRA SEEMA BAL", font=("Arial", 25, 'underline'))
blank_lbl.grid(row=1, column=1, columnspan=3)
# Use CTkButton instead of tkinter Button

lbl = Label(app, text="Upload master image file")
lbl.grid(row=2, column=1)
btn = Button(app, text="Upload", command=lambda: input_master())
btn.grid(row=2, column=2)

lbl2 = Label(app, text="Path to source image files")
lbl2.grid(row=3, column=1)
btn2 = Button(app, text="Select Directory", command=lambda: source_path())
btn2.grid(row=3, column=2)

lbl21 = Label(app, text="Path to copy matching faces")
lbl21.grid(row=4, column=1)
btn21 = Button(app, text="Select Destination Directory", command=lambda: destination_path())
btn21.grid(row=4, column=2)

btn3 = Button(app, text="Copy Images", command=lambda: search_faces())
btn3.grid(row=5, column=2)

btn2["state"] = "disabled"
btn21["state"] = "disabled"
btn3["state"] = "disabled"

success_msg = tk.StringVar()
lbl3 = tk.Label(app, textvariable=success_msg, fg="blue")
lbl3.grid(row=7, column=1)
success_msg.set("")

var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
lbl31 = tk.Label(app, textvariable=var1, fg="green")
lbl31.grid(row=2, column=3)
lbl32 = tk.Label(app, textvariable=var2, fg="green")
lbl32.grid(row=3, column=3)
lbl33 = tk.Label(app, textvariable=var3, fg="green")
lbl33.grid(row=4, column=3)
var1.set("")

itmsg = tk.Label(app, text="Created By: SOFTWARE CELL, FHQ SSB DELHI ", fg="green")
itmsg.grid(row=8, column=1)


def input_master():
    global source_image
    source_image = filedialog.askopenfilename(filetypes=[("IMAGE", "*.jpg")])
    if source_image != "":
        btn2["state"] = "enable"
    var1.set(source_image)
    root.update()
    return


def source_path():
    local_savefile = filedialog.askdirectory()
    global path
    path = local_savefile

    if local_savefile != "":
        btn21["state"] = "enable"
    var2.set(path)
    root.update()
    return


def destination_path():
    local_savefile = filedialog.askdirectory()
    global destination
    destination = local_savefile
    if local_savefile != "":
        btn3["state"] = "enable"
    var3.set(destination)
    root.update()
    return


def search_faces():
    success_msg.set("Please Wait...")
    root.update()
    # Load the jpg file into a numpy array
    sample = face_recognition.load_image_file(source_image)
    face_locations = face_recognition.face_locations(sample)
    sample_encode = face_recognition.face_encodings(sample)[0]

    # filelist = os.listdir(path)
    filelist = ["1.jpg"]
    print(filelist)

    for file in filelist:
        print(file)
        test = face_recognition.load_image_file(f"{path}/{file}")
        test_face_locations = face_recognition.face_locations(test)
        test_encodes = face_recognition.face_encodings(test)
        for test_encode in test_encodes:
            # test_encode = face_recognition.face_encodings(test)[0]
            results = face_recognition.compare_faces([sample_encode], test_encode, 0.5)
            distance = face_recognition.face_distance([sample_encode], test_encode)
            print(results, distance)
            if results[0] == True:
                shutil.copy(f"{path}/{file}", destination)

    success_msg.set("Completed Successfully")
    btn2["state"] = "disabled"
    btn21["state"] = "disabled"
    btn3["state"] = "disabled"
    print("File Converted Successfully")


root.mainloop()
