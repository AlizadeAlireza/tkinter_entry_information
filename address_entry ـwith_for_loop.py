import tkinter as tk

# Create a new window with the title "Address Entry Form"
window = tk.Tk()
window.title("Address Entry Form")

# a new frame to contain the Label and entry
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Pack the frame into the window 
frm_form.pack()

# List of field labels

labels = [
    "First Name:",
    "Last Name:",
    "Address:",
    "City:",
    "State:",
    "Postal Code:",
    "Country:",
]

# Loop over the list of field labels
for idx, text in enumerate(labels):
    # Create a Label widget with the text form the labels list
    label = tk.Label(master=frm_form, text=text)
    # Create an Entry widget
    entry = tk.Entry(master=frm_form, width=70)
    # Use the grid geometry manager to place the Lable and
    # Entry widgets in the eow whose index is idx
    label.grid(row=idx, column=0, sticky="e")
    entry.grid(row=idx, column=1)


# Create a new frame Button --> "frm_buttons"
# to contain submit and clear buttons

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx = 5, ipady = 5)


# Create the Submit button and pick it to the 
# right of "frm_buttons"

btn_submit = tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=6, ipady=6)

# Create the Submit button and pick it to the 
# right of "frm_buttons"

btn_clear = tk.Button(master=frm_buttons, text="Clear")
btn_clear.pack(side= tk.RIGHT, ipadx=10, ipady=6)



window.mainloop()