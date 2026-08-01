'''import tkinter as tk
def click():
    print("Button clicked")

window=tk.Tk()

button=tk.Button(window,text="Click Me",command=click)
button.pack()
window.mainloop()'''


import tkinter as tk
from tkinter import filedialog
def open_file():
    file=filedialog.askopenfilename()
    if file:
        f=open(file,"r")
        text.insert(tk.END,f.read())
        f.close()
root=tk.Tk()
tk.Button(root,text="open file",command=open_file).pack()
text=tk.Text(root)
text.pack()
root.mainloop()

