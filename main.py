import customtkinter

app = customtkinter.CTk()
app.title("Fly Penguin")
app.geometry("900x700")

#4 by 4 grid 
for i in range(4):
     app.columnconfigure(i, weight=1)

#tabs
tabview = customtkinter.CTkTabview(app)
tabview.grid(row=0, column=0)

tabview.add("tab 1")  # add tab at the end
tabview.add("tab 2")  # add tab at the end
tabview.set("tab 2")  # set currently visible tab


main_title = customtkinter.CTkLabel(tabview.tab("tab 2"), text="Welcome To Fly Penguin",text_color="white", font=("Bahnschrift",60) )
main_title.grid(row=1, column=1, padx=20, columnspan=2, pady=20)

#buttons
main_button_searchflights = customtkinter.CTkButton(tabview.tab("tab 2"), text="Search Flights", font=("Bahnschrift", 30), height=60, width=250)
main_button_searchflights.grid(row=2, column=1, columnspan=2)

main_button_bookflight = customtkinter.CTkButton(tabview.tab("tab 2"), text="Book Flight", font=("Bahnschrift", 30), height=60, width=250)
main_button_bookflight.grid(row=3, column=1, columnspan=2)

main_button_cancel = customtkinter.CTkButton(tabview.tab("tab 2"), text="Cancel Booking", font=("Bahnschrift", 30), height=60, width=250)
main_button_cancel.grid(row=4, column=1, columnspan=2)

app.mainloop()