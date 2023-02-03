from tkinter.constants import END

import customtkinter
import tkinter
import openai

openai.api_key = "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"

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x540")


def button_function():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=entry.get(),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    output_msg = response["choices"][0].get("text")
    print(response["choices"][0].get("text"))
    tk_textbox.delete('0.0', END)
    tk_textbox.insert('0.0', output_msg)


frame = customtkinter.CTkFrame(master=app,
                               width=800,
                               height=600,
                               corner_radius=10,
                               fg_color="light grey",
                               border_color="dark_blue")
frame.grid(padx=20, pady=20)

blank_lbl = customtkinter.CTkLabel(master=frame, text="  ")
blank_lbl.grid(row=0, column=2)
# Use CTkButton instead of tkinter Button

lbl_input = customtkinter.CTkLabel(master=frame, text="Enter your query           ")
lbl_input.grid(row=2, column=1)
entry = customtkinter.CTkEntry(master=frame, width=500)
entry.grid(row=2, column=2)

lbl_output1 = customtkinter.CTkLabel(master=frame, text="Generated Text")
lbl_output1.grid(row=3, column=1)

# create scrollable textbox
tk_textbox = customtkinter.CTkTextbox(master=frame, width=500, height=400)
tk_textbox.grid(row=3, column=2)

blank_lbl.grid(row=4, column=2)
blank_lbl.grid(row=5, column=2)

button = customtkinter.CTkButton(master=frame, text="GENERATE", command=button_function)
button.grid(row=6, column=2)
blank_lbl.grid(row=7, column=2)
blank_lbl.grid(row=6, column=3)

close_button = customtkinter.CTkButton(master=frame, text="CLOSE", command=app.destroy)
close_button.grid(row=7, column=2)

itmsg = customtkinter.CTkLabel(master=frame, text="Created By: SOFTWARE CELL, FHQ SSB DELHI ")
itmsg.grid(row=9, column=1)

app.mainloop()
