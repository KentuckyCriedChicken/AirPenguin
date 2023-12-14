import customtkinter

app = customtkinter.CTk()
app.title("Fly Penguin")
app.geometry("900x700")
#app.iconbitmap("C:/Users/Mohammed Kaif/Downloads/Screenshot 2023-08-16 132550.ico")

frame = customtkinter.CTkFrame(app, width = 200, height = 200)
app.columnconfigure(0, weight=1)
frame.grid(row=0, column=0)

label = customtkinter.CTkLabel(app, text="Welcome To Fly Penguin",text_color="white")
label.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()