print("BoardTool")
print("For help:")
print("Contact my email(gdKid67@gmail.com)")


import tkinter as tk
from tkinter import filedialog
def file_open():
    def export():
        types = [("KiCAD PCB", "*.kicad_pcb"),
             ("All files", "*.*")]
        file = filedialog.asksaveasfile(title = "Export",
                                    initialdir = ".",
                                    defaultextension=".kicad_pcb",
                                    filetypes=types)
    
    root = tk.Tk()
    root.title("file")
    export = tk.Button(root, text="Export", command=export)
    export.pack()

    import_BT_Function = tk.Button(root, text="Import")
    import_BT_Function.pack()



root = tk.Tk()
root.title("BoardTool 0.0.1")
root.minsize(500, 500) #(Width, Height)
file = tk.Button(root, text="File", command=file_open)
file.pack()

print("Opened BoardTool")

root.mainloop()
print("Closed BoardTool")
