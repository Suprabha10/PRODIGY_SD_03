import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load existing contacts from the file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add new contact
def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    
    if name and phone and email:
        contacts[name] = {"Phone": phone, "Email": email}
        save_contacts(contacts)
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "All fields are required.")

# Update the contact listbox
def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        listbox_contacts.insert(tk.END, contact)

# Clear entry fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Edit selected contact
def edit_contact():
    selected_contact = listbox_contacts.get(tk.ACTIVE)
    if selected_contact:
        entry_name.delete(0, tk.END)
        entry_name.insert(0, selected_contact)
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contacts[selected_contact]["Phone"])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contacts[selected_contact]["Email"])
        delete_contact()

# Delete selected contact
def delete_contact():
    selected_contact = listbox_contacts.get(tk.ACTIVE)
    if selected_contact:
        del contacts[selected_contact]
        save_contacts(contacts)
        update_contact_list()
        clear_entries()

# Initialize contacts
contacts = load_contacts()

# Set up the main window
window = tk.Tk()
window.title("Contact Management System")
window.geometry("400x500")
window.resizable(False, False)

# UI Elements
frame_top = tk.Frame(window)
frame_top.pack(pady=10)

label_name = tk.Label(frame_top, text="Name:", font=("Arial", 12))
label_name.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_name = tk.Entry(frame_top, width=30, font=("Arial", 12))
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_phone = tk.Label(frame_top, text="Phone:", font=("Arial", 12))
label_phone.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_phone = tk.Entry(frame_top, width=30, font=("Arial", 12))
entry_phone.grid(row=1, column=1, padx=5, pady=5)

label_email = tk.Label(frame_top, text="Email:", font=("Arial", 12))
label_email.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_email = tk.Entry(frame_top, width=30, font=("Arial", 12))
entry_email.grid(row=2, column=1, padx=5, pady=5)

frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10)

button_add = tk.Button(frame_buttons, text="Add Contact", width=15, command=add_contact, font=("Arial", 12))
button_add.grid(row=0, column=0, padx=5, pady=5)

button_edit = tk.Button(frame_buttons, text="Edit Contact", width=15, command=edit_contact, font=("Arial", 12))
button_edit.grid(row=0, column=1, padx=5, pady=5)

button_delete = tk.Button(frame_buttons, text="Delete Contact", width=15, command=delete_contact, font=("Arial", 12))
button_delete.grid(row=0, column=2, padx=5, pady=5)

frame_listbox = tk.Frame(window)
frame_listbox.pack(pady=10)

listbox_contacts = tk.Listbox(frame_listbox, width=50, height=15, font=("Arial", 12))
listbox_contacts.pack(side="left", fill="y")

scrollbar_contacts = tk.Scrollbar(frame_listbox, orient="vertical")
scrollbar_contacts.pack(side="right", fill="y")

listbox_contacts.config(yscrollcommand=scrollbar_contacts.set)
scrollbar_contacts.config(command=listbox_contacts.yview)

# Populate the contact list
update_contact_list()

# Run the application
window.mainloop()
