import tkinter as tk


# create new window with the title
window = tk.Tk()
window.title("Address Entry Form")

# a new frame to contain the Label and entry
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# pack the frame into the window
frm_form.pack()

# Label and entry for first_name
lbl_first_name = tk.Label(master=frm_form, text="First Name:")
ent_first_name = tk.Entry(master=frm_form, width=70)
# grid manager to place label and entry in first and second columns
# of the first row of grid
lbl_first_name.grid(row=0, column=0, sticky= "e")
ent_first_name.grid(row=0, column=1)

# Label and entry for last_name
lbl_last_name = tk.Label(master= frm_form, text="Last Name:")
ent_last_name = tk.Entry(master= frm_form, width=70)
# place the widgets in the second row of the grid
lbl_last_name.grid(row=1, column=0, sticky="e")
ent_last_name.grid(row=1, column=1)

# Label and entry for address_line
lbl_address = tk.Label(master= frm_form, text="Address:")
ent_address = tk.Entry(master= frm_form, width= 70)
# place the widgets in the third row of the grid
lbl_address.grid(row=3, column=0, sticky= "e")
ent_address.grid(row=3, column=1)

# Label and entry for city
lbl_city = tk.Label(master=frm_form, text="City:")
ent_city = tk.Entry(master=frm_form, width=70)
# place the widgets in the fourth row of the grid for city
lbl_city.grid(row=4, column=0, sticky= "e")
ent_city.grid(row=4, column=1)

# Label and entry for state
lbl_state = tk.Label(master=frm_form, text="State:")
ent_state = tk.Entry(master= frm_form, width= 70)
# place the widgets in the fifth row of the grid for state
lbl_state.grid(row=5, column=0, sticky= "e")
ent_state.grid(row=5, column=1)

# Label and entry for postal code
lbl_postal_code = tk.Label(master=frm_form, text="Postal Code:")
ent_postal_code = tk.Entry(master= frm_form, width=70)
# place the widgets in the sixth row of the grid for postal code
lbl_postal_code.grid(row=6, column=0, sticky= "e")
ent_postal_code.grid(row=6, column=1)

# Label and entry for country
lbl_country = tk.Label(master=frm_form, text="Country:")
ent_country = tk.Entry(master=frm_form, width= 70)
# place the widgets in the seventh row of the grid for country
lbl_country.grid(row=7, column=0, sticky= "e")
ent_country.grid(row=7, column=1)



# create a new frame for our buttons to contain
# Submit and Clear buttons.
# fill the whole windows in the horizontal direction
# 5 pixel padding 

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=6, ipady=6)


# create Submit button and pack it to the
# the right side of frm_buttons
btn_submit = tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=20,ipadx=10)

# create Submit button and pack it to the
# the right side of frm_buttons beside Submit button
btn_clear = tk.Button(master=frm_buttons, text="Clear")
btn_clear.pack(side=tk.RIGHT, ipadx=10)



window.mainloop()