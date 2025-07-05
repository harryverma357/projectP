import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    characters = ""
    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    length = int(length_slider.get())

    if not characters:
        messagebox.showwarning("Selection Needed", "Please select at least one character set.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    if auto_copy.get():
        copy_to_clipboard()

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

def toggle_password_visibility():
    if show_password.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


window = tk.Tk()
window.title("Advanced Password Generator")
window.geometry("450x400")
window.resizable(False, False)
window.configure(bg="#f0f0f0")


frame_options = tk.LabelFrame(window, text="Include Characters", padx=10, pady=10, bg="#f0f0f0")
frame_options.pack(pady=15)

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(frame_options, text="Uppercase (A-Z)", variable=var_upper, bg="#f0f0f0").grid(row=0, column=0, sticky="w")
tk.Checkbutton(frame_options, text="Lowercase (a-z)", variable=var_lower, bg="#f0f0f0").grid(row=1, column=0, sticky="w")
tk.Checkbutton(frame_options, text="Numbers (0-9)", variable=var_digits, bg="#f0f0f0").grid(row=0, column=1, sticky="w")
tk.Checkbutton(frame_options, text="Symbols (!@#$...)", variable=var_symbols, bg="#f0f0f0").grid(row=1, column=1, sticky="w")


tk.Label(window, text="Password Length", font=("Arial", 12), bg="#f0f0f0").pack()
length_slider = tk.Scale(window, from_=4, to=32, orient=tk.HORIZONTAL, length=300)
length_slider.set(12)
length_slider.pack(pady=10)


show_password = tk.BooleanVar()
tk.Checkbutton(window, text="Show Password", variable=show_password, command=toggle_password_visibility, bg="#f0f0f0").pack()

auto_copy = tk.BooleanVar(value=True)
tk.Checkbutton(window, text="Auto Copy to Clipboard", variable=auto_copy, bg="#f0f0f0").pack()


password_entry = tk.Entry(window, font=("Courier", 14), justify="center", show="*")
password_entry.pack(pady=15, ipady=5, ipadx=10)

tk.Button(window, text="Generate Password", font=("Arial", 12), command=generate_password).pack(pady=5)
tk.Button(window, text="Copy Manually", font=("Arial", 10), command=copy_to_clipboard).pack()

window.mainloop()
