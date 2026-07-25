# Simple GUI File Viewer using Tkinter

import tkinter as tk
from tkinter import filedialog, messagebox


def open_file():
    try:
       
        file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not file_path:
            return
        with open(file_path, "r") as file:
            content = file.read()       
        text_area.delete(1.0, tk.END)  
        text_area.insert(tk.END, content)    
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found!")
    except PermissionError:
        messagebox.showerror("Error", "Permission denied!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")
root = tk.Tk()
root.title("Simple File Viewer")
root.geometry("600x400")
open_button = tk.Button(
    root,
    text="Open File",
    command=open_file,
    font=("Arial", 12)
)
open_button.pack(pady=10)
text_area = tk.Text(root, wrap="word", font=("Arial", 11))
text_area.pack(expand=True, fill="both", padx=10, pady=10)
root.mainloop()
