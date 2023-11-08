from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("500x400")

set_appearance_mode("dark")

img = Image.open(
    r"G:\My Drive\Final Project Boris_E\Final Project\graphics\customtkinter-tutorial-master\Widgets\Button\upload.png")

btn = CTkButton(master=app, text="Upload Data", corner_radius=32, fg_color="#091e3d", 
                hover_color="#225c66", border_color="#c7c2b9", 
                border_width=2, image=CTkImage(dark_image=img, light_image=img))


btn.place(relx=0.5, rely=0.5, anchor="s") 

img = Image.open(
    r"G:\My Drive\Final Project Boris_E\Final Project\graphics\customtkinter-tutorial-master\Widgets\Button\configuration.png")

btn = CTkButton(master=app, text="Train Model", corner_radius=32, fg_color="#091e3d", 
                hover_color="#225c66", border_color="#c7c2b9", 
                border_width=2, image=CTkImage(dark_image=img, light_image=img))


btn.place(relx=0.5, rely=0.5, anchor="n") 

app.mainloop()


