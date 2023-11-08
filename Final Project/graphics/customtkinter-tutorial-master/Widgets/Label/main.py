from customtkinter import *

app = CTk()
app.geometry("500x400")

label = CTkLabel(master=app, text="Some Text...", font=("Minion Pro Med", 20), text_color="#d8f0ea")

label.place(relx=0.5, rely=0.5, anchor="center") 


app.mainloop()