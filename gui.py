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

# If a key is pressed, this callback function is triggered
def key_pressed(event):
    if(event.char == '\r'):
        convert_to_cm(event)  # if ENTER is pressed, convert the unit


# _______ GUI _____________________________________________________________
# Create a new window
window = tk.Tk()
window.title("Imperial-SI Units converter")
main_frame = tk.Frame(master = window)  # frame(panel) inside the window

#main_frame.rowconfigure(0, minsize = 80, weight = 1)   # Use if minimum size needs to be configured, weight for scaling
#main_frame.columnconfigure(1, minsize = 100, weight = 1)

# Entry (Text Area) for input
ent_unit = tk.Entry(master=main_frame, width = 15)
ent_unit.grid(row=0, column=0, padx=(15, 2), pady = 7)

lbl_imperial_unit = tk.Label(master=main_frame, text= "inch")
lbl_imperial_unit.grid(row=0, column=1, padx=(2, 5), pady = 10)

# Button for Conversion
#            Binding the button to a function:
#          a) attribute command = fcn_name, then the function has no extra argument
#          b) btn.bind("<Button-1>", fcn_name), then argument "event" needed
btn_convert = tk.Button(master=main_frame, text = "\N{RIGHTWARDS BLACK ARROW}", width = "3", height = "1")
btn_convert.grid(row=0, column=2, padx=(20,20), pady = 10)
btn_convert.bind("<Button-1>", convert_to_cm)

txt_result = "0 cm"
lbl_result = tk.Label(master=main_frame, text=txt_result)
lbl_result.grid(row=0, column=3, padx=(10,15), pady = 10)

# Add frame and create main loop for event handling
main_frame.pack()
window.bind("<Key>", key_pressed)  # key-event handling
window.mainloop()