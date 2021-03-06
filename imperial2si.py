# Sample demo of GUI Development with Tkinter
# Conversion calculator between imperial and metric units
# Created by: Krystof Hes
# 25.10.2020
# Based on a tutorial from: https://realpython.com/python-gui-tkinter/#building-a-temperature-converter-example-app

import tkinter as tk

# _______ FUNCTIONS ______________________________________________________
# Callback function for unit conversion
def convert_to_cm(event):
    input_value = float(ent_unit.get())
    result = input_value*2.54
    lbl_result["text"] = str(result) + " cm"
    print(str(input_value) + " inch = " + str(result) + " cm")

def convert_unit(event):
    input_unit = imp_unit.get()
    output_unit = SI_unit.get()
    input_value = float(ent_unit.get())
    factor = 1.0

    if input_unit == "inch":
        factor = 0.0254
    elif input_unit == "foot":
        factor  = 0.3048
    elif input_unit== "yard":
        factor  = 0.9144
    elif input_unit == "mile":
        factor = 1609.344
    elif input_unit == "nautical mile":
        factor = 1852

    if output_unit == "mm":
        factor *= 1000
    elif output_unit == "cm":
        factor *= 100
    elif output_unit == "km":
        factor *= 0.001
    lbl_result["text"] = str(input_value*factor)
    print(str(input_value*factor) + " "+ output_unit)

# If a key is pressed, this callback function is triggered
def key_pressed(event):
    if(event.char == '\r'):
        convert_unit(event)  # if ENTER is pressed, convert the unit

# Callback for change of StringVar imp_unit
def change_input_unit(*args):
    print("Input changed to: "+ imp_unit.get())
    convert_unit(0)

def change_output_unit(*args):
    print("Output changed to: " + SI_unit.get())
    convert_unit(0)

# _______ GUI _____________________________________________________________
# Create a new window
window = tk.Tk()
window.title("Imperial-SI Units converter")
main_frame = tk.Frame(master = window)  # frame(panel) inside the window

# Entry (Text Area) for input
ent_unit = tk.Entry(master=main_frame, width = 15)
ent_unit.grid(row=0, column=0, padx=(15, 2), pady = 7)

# Imperial Unit variable
imp_unit = tk.StringVar(window)
imperial_units = {'inch', 'foot', 'yard', 'mile', 'nautical mile'}   # dictionary for the dropdown menu
imp_unit.set('inch')   # default choice of the dropdown menu
imp_unit.trace('w', change_input_unit)   # call the callback function whenever the value changes

# Dropdown menu for unit selection
imp_unit_menu = tk.OptionMenu(main_frame, imp_unit, *imperial_units)
imp_unit_menu.grid(row=0, column=1, padx=(2, 5), pady = 10)

# Button for Conversion
#            Binding the button to a function:
#          a) attribute command = fcn_name, then the function has no extra argument
#          b) btn.bind("<Button-1>", fcn_name), then argument "event" needed
btn_convert = tk.Button(master=main_frame, text = "\N{RIGHTWARDS BLACK ARROW}", width = "3", height = "1")
btn_convert.grid(row=0, column=2, padx=(20,20), pady = 10)
btn_convert.bind("<Button-1>", convert_unit)

# SI Unit variable
SI_unit = tk.StringVar(window)
SI_units = {'mm', 'cm', 'm', 'km'}
SI_unit.set('m')
SI_unit.trace('w', change_output_unit)

# Result label
txt_result = "0"
lbl_result = tk.Label(master=main_frame, text=txt_result)
lbl_result.grid(row=0, column=3, padx=(10,15), pady = 10)

# Dropdown menu SI-unit
SI_unit_menu = tk.OptionMenu(main_frame, SI_unit, *SI_units)
SI_unit_menu.grid(row=0, column=4, padx=(10,15), pady=10)

# Add frame and create main loop for event handling
main_frame.pack()
window.bind("<Key>", key_pressed)  # key-event handling
window.mainloop()