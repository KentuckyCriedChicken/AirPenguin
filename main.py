import customtkinter

app = customtkinter.CTk()
app.title("Fly Penguin")
app.geometry("900x700")
#app.iconbitmap("C:/Users/Mohammed Kaif/Downloads/Screenshot 2023-08-16 132550.ico")

#4 by 4 grid 
for i in range(4):
    app.columnconfigure(i, weight=1)


def Main_Menu():
    main_title = customtkinter.CTkLabel(app, text="Welcome To Fly Penguin",text_color="white", font=("Bahnschrift",60) )
    main_title.grid(row=1, column=1, padx=20, columnspan=2, pady=20)

    main_frame = customtkinter.CTkFrame(app, width=600, height=500)
    main_frame.grid(row=2, column=0, rowspan=3, columnspan=4, pady=20)

    #buttons
    main_button_searchflight = customtkinter.CTkButton(app, text="Search Flight", font=("Bahnschrift", 30), height=60, width=250)
    main_button_searchflight.grid(row=2, column=1, columnspan=2)

    main_button_bookflight = customtkinter.CTkButton(app, text="Book Flight", font=("Bahnschrift", 30), height=60, width=250)
    main_button_bookflight.grid(row=3, column=1, columnspan=2)

    main_button_cancel = customtkinter.CTkButton(app, text="Cancel Booking", font=("Bahnschrift", 30), height=60, width=250)
    main_button_cancel.grid(row=4, column=1, columnspan=2)

    app.mainloop()

Main_Menu()

  