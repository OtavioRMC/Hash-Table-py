
import tkinter as tk
from tkinter import messagebox
from HashTable.utils import *
from HashTable.hash import HashTable

class Application(tk.Frame):
   def __init__(self, master=None):
       super().__init__(master)
       self.master = master
       self.pack()
       self.create_widgets()

   def create_widgets(self):
       self.name_label = tk.Label(self, text="Name")
       self.name_label.pack(side="top", pady=(20, 10))

       self.name_entry = tk.Entry(self)
       self.name_entry.pack(side="top", ipady=5)

       self.address_label = tk.Label(self, text="Address")
       self.address_label.pack(side="top", pady=10)

       self.address_entry = tk.Entry(self)
       self.address_entry.pack(side="top", ipady=5)

       self.telephone_label = tk.Label(self, text="Telephone Number")
       self.telephone_label.pack(side="top", pady=10)

       self.telephone_entry = tk.Entry(self)
       self.telephone_entry.pack(side="top", ipady=5)

       self.insert_button = tk.Button(self, text="Insert Contact", command=self.insert_contact)
       self.insert_button.pack(side="top", pady=10)

       self.search_button = tk.Button(self, text="Search Contact", command=self.search_contact)
       self.search_button.pack(side="top", pady=10)

       self.remove_button = tk.Button(self, text="Remove Contact", command=self.remove_contact)
       self.remove_button.pack(side="top", pady=(10, 20))

       self.hash_table = HashTable(100)

   def insert_contact(self):
       name = self.name_entry.get()
       address = self.address_entry.get()
       telephone_number = self.telephone_entry.get()
       self.hash_table.set(name, Contact(name, address, telephone_number))

   def search_contact(self):
       name = self.name_entry.get()
       try:
          contact = self.hash_table.get(name)
          messagebox.showinfo("Contact Details", f"Name: {contact.name}, Address: {contact.address}, Telephone Number: {contact.telephone_number}")
       except KeyError:
          messagebox.showerror("Error", "Contact not found")

   def remove_contact(self):
       name = self.name_entry.get()
       try:
          self.hash_table.remove(name)
          messagebox.showinfo("Success", "Contact removed")
       except KeyError:
          messagebox.showerror("Error", "Contact not found")

root = tk.Tk()
app = Application(master=root)
app.mainloop()