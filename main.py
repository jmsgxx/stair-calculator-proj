from tkinter import *
import math
from tkinter import messagebox

MAX_RISER = 175
MIN_TREAD = 250
MAX_STEPS = 16
CALC_BUTTON = "#8CB5BF"
CLEAR_B = "#C17587"
TXT_BUTTON = "#F2E6DE"
CANV_BG = "#DAA5A4"
WX = "400"
WY = "350"

#----------------------------CALCULATE FUNCTION----------------------------------#

def calculate():
    try:
        base_level = float(base_level_entry.get())
        top_level = float(top_level_entry.get())

    except ValueError:
        messagebox.showinfo(title="Error", message="Please input a proper number")
        base_level_entry.focus()
        base_level_entry.delete(0, END)
        top_level_entry.delete(0, END)

    else:
        floor_height = top_level - base_level
        floor_height_entry.insert(0, int(floor_height))
        steps_number = math.ceil(floor_height / MAX_RISER)
        steps_number_entry.insert(0, steps_number)
        actual_riser = floor_height / steps_number
        actual_riser_entry.insert(0, round(actual_riser,2))
        min_num_flight = math.ceil(steps_number / MAX_STEPS)
        min_no_flights_entry.insert(0, min_num_flight)
        total_run = (MIN_TREAD * steps_number) / min_num_flight
        total_run_length_entry.insert(0, int(total_run))

def clear_entry():
    base_level_entry.delete(0, END)
    top_level_entry.delete(0, END)
    floor_height_entry.delete(0, END)
    steps_number_entry.delete(0, END)
    actual_riser_entry.delete(0, END)
    min_no_flights_entry.delete(0, END)
    total_run_length_entry.delete(0, END)
    base_level_entry.focus()


#----------------------------UI SET UP----------------------------------#

window = Tk()
window.title("Stair Calculator")
window.config(padx=30, pady=30, bg="white")

# Set the size of the window
window.geometry(f"{WX}x{WY}")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the position of the window
x = (screen_width / 2) - (int(WX) / 2)
y = (screen_height / 2) - (int(WY) / 2)

# Set the position of the window
window.geometry(f"+{int(x)}+{int(y)}")



# LABELS
max_riser_label = Label(text=f"Max. riser requirement: {MAX_RISER}mm",bg="white")
max_riser_label.grid(row=1, column=0, columnspan=2)
min_tread_label = Label(text=f"Min. tread depth: {MIN_TREAD}mm",bg="white")
min_tread_label.grid(row=2, column=0, columnspan=2)
base_level_label = Label(text="BASE LEVEL:",bg="white")
base_level_label.grid(row=3, column=0)
top_level_label = Label(text="TOP LEVEL:",bg="white")
top_level_label.grid(row=4, column=0)
floor_height_label = Label(text="Floor to floor ht:",bg="white")
floor_height_label.grid(row=6, column=0)
total_steps_label = Label(text="Total steps:",bg="white")
total_steps_label.grid(row=7, column=0)
actual_riser_label = Label(text="Actual riser:",bg="white")
actual_riser_label.grid(row=8, column=0)
min_num_flight_label = Label(text="Min. no. of flight:",bg="white")
min_num_flight_label.grid(row=9, column=0)
max_step_label = Label(text=f"Max. steps\n(excluding landing): {MAX_STEPS}",bg="white")
max_step_label.grid(row=10, column=0)
total_run_length = Label(text="Min. run length\n(for single flight):",bg="white")
total_run_length.grid(row=11, column=0)

# BUTTON
calculate_button = Button(text="Calculate", width=40, bg=CALC_BUTTON, command=calculate, font=("Arial", 10, "bold"))
calculate_button.grid(row=5, column=0,columnspan=4)
clear_button = Button(text="Clear all", width=40, bg=CLEAR_B, command=clear_entry, font=("Arial", 10, "bold"))
clear_button.grid(row=12, column=0,columnspan=4)

# ENTRY
base_level_entry = Entry(width=30, highlightthickness=1)
base_level_entry.grid(row=3, column=1)
base_level_entry.focus()
top_level_entry = Entry(width=30, highlightthickness=1)
top_level_entry.grid(row=4, column=1)

# RESULT ENTRY
floor_height_entry = Entry(width=30, highlightthickness=1)
floor_height_entry.grid(row=6, column=1)
steps_number_entry = Entry(width=30, highlightthickness=1)
steps_number_entry.grid(row=7, column=1)
actual_riser_entry = Entry(width=30, highlightthickness=1)
actual_riser_entry.grid(row=8, column=1)
min_no_flights_entry = Entry(width=30, highlightthickness=1)
min_no_flights_entry.grid(row=9, column=1)
total_run_length_entry = Entry(width=30)
total_run_length_entry.grid(row=11, column=1)


# pyinstaller --noconsole --icon=youricon.ico yourscriptname.py



window.mainloop()