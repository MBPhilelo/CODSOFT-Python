import tkinter as tk
from tkinter import messagebox

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.contacts = []

        # Create main frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        # Create a canvas
        self.canvas = tk.Canvas(self.main_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add a scrollbar to the canvas
        self.scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Create another frame inside the canvas
        self.scrollable_frame = tk.Frame(self.canvas)

        # Add that new frame to a window in the canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Create GUI components
        self.title_label = tk.Label(self.scrollable_frame, text="Contact Manager", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.name_label = tk.Label(self.scrollable_frame, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.scrollable_frame)
        self.name_entry.pack(pady=5)

        self.phone_label = tk.Label(self.scrollable_frame, text="Phone Number:")
        self.phone_label.pack(pady=5)
        self.phone_entry = tk.Entry(self.scrollable_frame)
        self.phone_entry.pack(pady=5)

        self.email_label = tk.Label(self.scrollable_frame, text="Email:")
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(self.scrollable_frame)
        self.email_entry.pack(pady=5)

        self.address_label = tk.Label(self.scrollable_frame, text="Address:")
        self.address_label.pack(pady=5)
        self.address_entry = tk.Entry(self.scrollable_frame)
        self.address_entry.pack(pady=5)

        self.add_button = tk.Button(self.scrollable_frame, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=10)

        # Create a frame for the listbox and scrollbar
        self.listbox_frame = tk.Frame(self.scrollable_frame)
        self.listbox_frame.pack(pady=10)

        self.scrollbar_listbox = tk.Scrollbar(self.listbox_frame, orient=tk.VERTICAL)
        self.contact_listbox = tk.Listbox(self.listbox_frame, width=50, height=10, yscrollcommand=self.scrollbar_listbox.set)
        self.scrollbar_listbox.config(command=self.contact_listbox.yview)
        self.scrollbar_listbox.pack(side=tk.RIGHT, fill=tk.Y)
        self.contact_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.contact_listbox.bind('<<ListboxSelect>>', self.load_selected_contact)

        self.update_button = tk.Button(self.scrollable_frame, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.scrollable_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

        self.search_label = tk.Label(self.scrollable_frame, text="Search by Name or Phone:")
        self.search_label.pack(pady=5)
        self.search_entry = tk.Entry(self.scrollable_frame)
        self.search_entry.pack(pady=5)
        self.search_button = tk.Button(self.scrollable_frame, text="Search", command=self.search_contact)
        self.search_button.pack(pady=5)

        self.reset_button = tk.Button(self.scrollable_frame, text="Reset", command=self.reset_fields)
        self.reset_button.pack(pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
            self.update_contact_listbox()
            self.reset_fields()
        else:
            messagebox.showwarning("Warning", "Name and Phone Number are required.")

    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def load_selected_contact(self, event):
        try:
            index = self.contact_listbox.curselection()[0]
            contact = self.contacts[index]

            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, contact['name'])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(tk.END, contact['phone'])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(tk.END, contact['email'])
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(tk.END, contact['address'])
        except IndexError:
            pass

    def update_contact(self):
        try:
            index = self.contact_listbox.curselection()[0]
            self.contacts[index] = {
                'name': self.name_entry.get(),
                'phone': self.phone_entry.get(),
                'email': self.email_entry.get(),
                'address': self.address_entry.get()
            }
            self.update_contact_listbox()
            self.reset_fields()
        except IndexError:
            messagebox.showwarning("Warning", "Select a contact to update.")

    def delete_contact(self):
        try:
            index = self.contact_listbox.curselection()[0]
            del self.contacts[index]
            self.update_contact_listbox()
            self.reset_fields()
        except IndexError:
            messagebox.showwarning("Warning", "Select a contact to delete.")

    def search_contact(self):
        query = self.search_entry.get().lower()
        filtered_contacts = [contact for contact in self.contacts if query in contact['name'].lower() or query in contact['phone']]
        self.contact_listbox.delete(0, tk.END)
        for contact in filtered_contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def reset_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)
        self.update_contact_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
