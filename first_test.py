import customtkinter

app = customtkinter.CTk()
app.title("Fly Penguin")
app.geometry("900x700")
app.iconbitmap("C:/Users/Mohammed Kaif/Downloads/Screenshot 2023-08-16 132550.ico")
app.grid_columnconfigure(0, weight=1)

label = customtkinter.CTkLabel(app, text="Welcome To Fly Penguin", fg_color="transparent", text_color="white")
label.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()