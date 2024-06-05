import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import subprocess

import argparse
import getpass
import sys
import hashlib


def authenticate():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    hash_object = hashlib.sha256()
    hash_object.update(entered_password.encode())
    hashed_string = hash_object.hexdigest()

    correct_password = 'a1159e9df3670d549d04524532629f5477ceb7deec9b45e47e8c009506ecb2c8'

    if(hashed_string==correct_password):
        run_whitelist()
    else:
        show_error_message("Incorrect Password")

def run_whitelist():
    subprocess.run(['python', 'whitelist.py'], check=True)
    messagebox.showinfo("Authentication Successful", "Whitelist.py is running!")

def show_error_message(message):
    messagebox.showerror("Authentication Error", message)

# Create the main window
auth_window = tk.Tk()
auth_window.title("Application Whitelisting Auth")
auth_window.geometry("300x150")

# Style
style = ttk.Style()
style.configure("TButton", padding=(10, 5, 10, 5), font='Helvetica 10')

# Username entry
username_label = tk.Label(auth_window, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(auth_window)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Password entry
password_label = tk.Label(auth_window, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(auth_window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Submit button
submit_button = ttk.Button(auth_window, text="Submit", command=authenticate, style="TButton")
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the authentication window loop
auth_window.mainloop()
