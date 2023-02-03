from tkinter.constants import *
from tkinter.ttk import *
from tkinter import scrolledtext, font as TkFont
import tkinter as tk
import openai
from datetime import date

openai.api_key = "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"

root = tk.Tk()  # create CTk window like you do with the Tk window
root.geometry("700x650")

app = Frame(root)
app.place(x=10, y=5)


def button_function():
    success_msg.set("Please Wait . . . ")
    app.update()
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=entry.get('0.0', END),
        temperature=0.7,
        max_tokens=3072,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    global output_msg
    output_msg = response["choices"][0].get("text")
    print(response["choices"][0].get("text"))
    tk_textbox["state"] = "normal"
    tk_textbox.delete(0.0, END)
    tk_textbox.insert(0.0, output_msg)
    tk_textbox["state"] = "disabled"
    success_msg.set("")
    copy_button["state"] = "enable"
    app.update()


def copy_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_msg)


blank_lbl = Label(app, text="SASHASTRA SEEMA BAL", font=("Arial", 25, 'underline'))
blank_lbl.grid(row=1, column=1)
# Use CTkButton instead of tkinter Button

lbl_input = Label(app, text="Enter your query", font=("Arial", 12))
lbl_input.grid(row=2, column=1)
entry = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=80, height=5)
entry.grid(row=3, column=1)
# entry = Entry(app, width=109)
# entry.grid(row=2, column=2)

# lbl_output1 = Label(app, text="Generated Text")
# lbl_output1.grid(row=4, column=1)
button = Button(app, text="GENERATE TEXT", command=button_function, width=25)
button.grid(row=4, column=1)

tk_textbox = scrolledtext.ScrolledText(app, wrap=tk.WORD)
tk_textbox.grid(row=5, column=1)
tk_textbox["state"] = "disabled"

success_msg = tk.StringVar()
lbl3 = tk.Label(app, textvariable=success_msg, fg="#256ef5")
lbl3.grid(row=6, column=1)
success_msg.set("")

close_button = Button(app, text="CLOSE", command=root.destroy, width=25)
close_button.grid(row=7, column=1, sticky='e')

copy_button = Button(app, text="Copy Text", command=copy_clipboard, width=25)
copy_button.grid(row=7, column=1, sticky='w')
copy_button["state"] = "disabled"

itmsg = tk.Label(app, text="Created By: SOFTWARE CELL, FHQ SSB DELHI ", fg="green")
itmsg.grid(row=9, column=1)

today = date.today()
year = today.strftime("%Y")

if int(year) == 2022:
    root.mainloop()
