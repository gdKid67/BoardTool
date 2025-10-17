print("BoardTool")
print("For help:")
print("Contact my email(gdKid67@gmail.com)")


import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.title("BoardTool 0.0.1")
root.minsize(500, 500) #(Width, Height)

print("Opened BoardTool[ 1/2 windows ]")

root = tk.Tk()
root.title("Controls")

def export():
    types = [("KiCAD PCB", "*.kicad_pcb"),
             ("All files", "*.*")]
    file = filedialog.asksaveasfile(title = "Export",
                                    initialdir = ".",
                                    defaultextension=".kicad_pcb",
                                    filetypes=types)

export = tk.Button(root, text="Export", command=export)
export.pack()

import_BT_Function = tk.Button(root, text="Import")
import_BT_Function.pack()

print("Opened BoardTool[ 2/2 windows]")

root.mainloop()
print("Closed BoardTool")
