# Sample demo of GUI Development with Tkinter
# Text editor
# Created by: Krystof Hes
# 25.10.2020
# Based on a tutorial from: https://realpython.com/python-gui-tkinter/#building-a-temperature-converter-example-app


import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

# _______ FUNCTIONS ______________________________________________________
def open_file():
    print("Choose a file to open")
    # Open the dialog window and pick a file
    path = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not path:
        return
    # Read the file
    with open(path, 'r') as input_file:
        text = input_file.read()
        text_area.delete(0.0, tk.END) # delete content
        text_area.insert(0.0, text)   # insert text to the text area
    # Display path in the window
    lbl_path["text"] = str(path)

def save_file():
    print("Choose where to save the file")
    # Open the dialog
    path = asksaveasfilename(
        defaultextension = ".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not path:
        return

    # Save the file
    with open(path, "w") as ouput_file:
        text = text_area.get("1.0", tk.END)
        ouput_file.write(text)
    lbl_path["text"] = path + "."
    print("Saving file...")


# _______ GUI _____________________________________________________________

# Window
window = tk.Tk()
window.title("Simplest text editor")
frame_ctrl = tk.Frame(master = window)   # control panel
frame_edit = tk.Frame(master = window)   # text area panel

# Open button
btn_open = tk.Button(frame_ctrl, text = "Open", command=open_file)
btn_open.grid(row=0, column=0)

# Save button
btn_save = tk.Button(frame_ctrl, text = "Save", command=save_file)
btn_save.grid(row=0, column=1)

# Path label
lbl_path = tk.Label(frame_ctrl, text="")
lbl_path.grid(row=0, column=2, sticky="ew")

# Text Area (Text)
text_area = tk.Text(frame_edit, width = 80, height = 20)
text_area.pack()

# Overall Layout
frame_ctrl.grid(row=0, column=0)
frame_edit.grid(row=1, column=0)
# Loop
window.mainloop()