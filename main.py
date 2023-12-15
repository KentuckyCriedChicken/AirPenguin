import customtkinter

app = customtkinter.CTk()
app.title("Fly Penguin")
app.geometry("900x700")

#4 by 4 grid 
for i in range(4):
     app.columnconfigure(i, weight=1)

main_title = customtkinter.CTkLabel(app, text="Welcome To Fly Penguin",text_color="white", font=("Bahnschrift",60) )
main_title.grid(row=1, column=1, padx=20, columnspan=2, pady=20)



#tabs
tabview = customtkinter.CTkTabview(app,width=600, height=500)
tabview.grid(row=2, column=0, rowspan=3, columnspan=4, pady=20)

search_flights = tabview.add("Search for flights")  
book_flight = tabview.add("Book a flight")  
cancel_booking = tabview.add("Cancel your booking") 
tabview.set("Search for flights")



#search for flight
customtkinter.CTkLabel(search_flights, text='Enter Boarding:', font=("Bahnschrift", 30) ).grid(row=2, column=0, sticky='w', pady=40)
customtkinter.CTkLabel(search_flights, text='Enter Destination:', font=("Bahnschrift", 30) ).grid(row=3, column=0,sticky='w', pady=40)
customtkinter.CTkLabel(search_flights, text='Choose Day of Travel:', font=("Bahnschrift", 30) ).grid(row=4, column=0,sticky='w',pady=40)

sboarding = customtkinter.CTkOptionMenu(search_flights, width=200, values=["New York City", "Dubai", "Paris", "Delhi", "Singapore", "London"], anchor="center")
sboarding.grid(row=2, column=1, padx=40)

sdestination = customtkinter.CTkOptionMenu(search_flights, width=200, values=["New York City", "Dubai", "Paris", "Delhi", "Singapore", "London"], anchor="center")
sdestination.grid(row=3, column=1, padx=40)

sday = customtkinter.CTkOptionMenu(search_flights, width=200, values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], anchor="center")
sday.grid(row=4, column=1, padx=40)

search = customtkinter.CTkButton(search_flights, text="Search", height=40, width=200, font=("Bahnschrift", 25 ), fg_color="#525252", hover_color="#808080")
search.grid(row=5, column=0, columnspan=2, pady=15)


#Book a flight
customtkinter.CTkLabel(book_flight, text='Enter Boarding:', font=("Bahnschrift", 20) ).grid(row=2, column=0, sticky='w', pady=15)
customtkinter.CTkLabel(book_flight, text='Enter Destination:', font=("Bahnschrift", 20) ).grid(row=3, column=0,sticky='w', pady=15)
customtkinter.CTkLabel(book_flight, text='Enter last 4 digit of Aadhar Number:', font=("Bahnschrift", 20) ).grid(row=4, column=0,sticky='w',pady=15)
customtkinter.CTkLabel(book_flight, text='Choose Class:', font=("Bahnschrift", 20) ).grid(row=5, column=0, sticky='w', pady=15)
customtkinter.CTkLabel(book_flight, text='Choose Day of Travel:', font=("Bahnschrift", 20) ).grid(row=6, column=0,sticky='w', pady=15)
customtkinter.CTkLabel(book_flight, text='Choose Time of Flight:', font=("Bahnschrift", 20) ).grid(row=7, column=0,sticky='w',pady=15)

bboarding = customtkinter.CTkOptionMenu(book_flight, width=200, height=25, values=["New York City", "Dubai", "Paris", "Delhi", "Singapore", "London"], anchor="center")
bboarding.grid(row=2, column=1, padx=40)

bdestination = customtkinter.CTkOptionMenu(book_flight, width=200, height=25, values=["New York City", "Dubai", "Paris", "Delhi", "Singapore", "London"], anchor="center")
bdestination.grid(row=3, column=1, padx=40)

baadhar = customtkinter.CTkEntry(book_flight, width=200, height=25, fg_color="#1F6AA5")
baadhar.grid(row=4, column=1, padx=40)

bclass = customtkinter.CTkOptionMenu(book_flight, width=200, height=25, values=["Economy Class", "Business Class"], anchor="center")
bclass.grid(row=5, column=1, padx=40)

bday = customtkinter.CTkOptionMenu(book_flight, width=200, height=25, values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], anchor="center")
bday.grid(row=6, column=1, padx=40)

btime = customtkinter.CTkOptionMenu(book_flight, width=200, height=25, values=["10pm", "1am", "3am"], anchor="center")
btime.grid(row=7, column=1, padx=40)

book = customtkinter.CTkButton(book_flight, text="Book", height=40, width=200, font=("Bahnschrift", 25 ), fg_color="#525252", hover_color="#808080")
book.grid(row=8, column=0, columnspan=2, pady=15)


#Cancel a flight
customtkinter.CTkLabel(cancel_booking, text='Enter last 4 digit of Aadhar Number:', font=("Bahnschrift", 20) ).grid(row=2, column=0,sticky='w',pady=15)
customtkinter.CTkLabel(cancel_booking, text='Choose Class:', font=("Bahnschrift", 20) ).grid(row=3, column=0, sticky='w', pady=15)
customtkinter.CTkLabel(cancel_booking, text='Enter Boarding:', font=("Bahnschrift", 20) ).grid(row=4, column=0, sticky='w', pady=15)

caadhar = customtkinter.CTkEntry(cancel_booking, width=200, height=25, fg_color="#1F6AA5")
caadhar.grid(row=2, column=1, padx=40)

cclass = customtkinter.CTkOptionMenu(cancel_booking, width=200, height=25, values=["Economy Class", "Business Class"], anchor="center")
cclass.grid(row=3, column=1, padx=40)

cboarding = customtkinter.CTkOptionMenu(cancel_booking, width=200, height=25, values=["New York City", "Dubai", "Paris", "Delhi", "Singapore", "London"], anchor="center")
cboarding.grid(row=4, column=1, padx=40)

cancel = customtkinter.CTkButton(cancel_booking, text="Cancel booking", height=40, width=200, font=("Bahnschrift", 23 ), fg_color="#525252", hover_color="#808080")
cancel.grid(row=5, column=0, columnspan=2, pady=25)

app.mainloop()