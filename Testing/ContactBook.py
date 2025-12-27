import tkinter as tk
import json

# ---------- File handling ----------
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

contacts = load_contacts()

# ---------- Functions ----------
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    if name == "" or phone == "":
        output.insert(tk.END, "Please enter name and phone.\n")
        return

    contacts[name] = phone
    save_contacts()
    output.insert(tk.END, f"Added: {name} - {phone}\n")

def view_contacts():
    output.delete(1.0, tk.END)
    if not contacts:
        output.insert(tk.END, "No contacts found.\n")
    else:
        for name, phone in contacts.items():
            output.insert(tk.END, f"{name}: {phone}\n")

def search_contact():
    name = name_entry.get()
    output.delete(1.0, tk.END)

    if name in contacts:
        output.insert(tk.END, f"{name}: {contacts[name]}\n")
    else:
        output.insert(tk.END, "Contact not found.\n")

def delete_contact():
    name = name_entry.get()

    if name in contacts:
        del contacts[name]
        save_contacts()
        output.insert(tk.END, f"Deleted: {name}\n")
    else:
        output.insert(tk.END, "Contact not found.\n")

# ---------- GUI ----------
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x400")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="View Contacts", command=view_contacts).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

output = tk.Text(root, height=10)
output.pack(pady=10)

root.mainloop()
