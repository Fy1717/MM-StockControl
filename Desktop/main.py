import tkinter as tk
import sqlite3
from tkinter import messagebox

from database import Database
from product import Product

def showMessage(message1, message2):
    messagebox.showinfo(" " + message1 +" \r\n", message2)
        
def showWordsScreen(products):
    root= tk.Tk()
    root.title("ALL PRODUCTS")
    root.geometry("320x200")
        
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y )

    mylist = tk.Listbox(root, yscrollcommand = scrollbar.set, width=300)
    for p in products:
        prod = "Id: " +  str(p[0]) + "  Name: " + str(p[1]).upper() + "  Referans: " + str(p[2]).upper() + "  Count: " + str(p[3])
        mylist.insert(tk.END, prod)

    mylist.pack(side = tk.LEFT, fill = tk.BOTH)
    scrollbar.config( command = mylist.yview )
    
    root.mainloop()

class ProductApp(tk.Tk):
    db = Database("D://mydatabase.db")
    print("\nConnected To Database")
        
    product = Product(db)
    product.create_table()
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Mikron Makina - Stok Takip")
        
        self.empty0_label = tk.Label(self, text="")
        self.empty0_label.grid(row=0, column=0)
        
        self.name_label = tk.Label(self, text="Name : ")
        self.name_label.grid(row=1, column=1)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=2)
        
        self.reference_label = tk.Label(self, text="Reference :")
        self.reference_label.grid(row=2, column=1)
        self.reference_entry = tk.Entry(self)
        self.reference_entry.grid(row=2, column=2)
        
        self.count_label = tk.Label(self, text="Count : ")
        self.count_label.grid(row=3, column=1)
        self.count_entry = tk.Entry(self)
        self.count_entry.grid(row=3, column=2)
        
        self.empty_label = tk.Label(self, text="")
        self.empty_label.grid(row=4, column=0)
        
        self.empty2_label = tk.Label(self, text="")
        self.empty2_label.grid(row=5, column=0)
        
        self.create_button = tk.Button(self, text="Create", command=self.create_product, width=17)
        self.create_button.grid(row=6, column=0)
                
        self.read_button = tk.Button(self, text="Read", command=self.read_products, width=17)
        self.read_button.grid(row=6, column=1)
        
        self.update_button = tk.Button(self, text="Update", command=self.update_product, width=17)
        self.update_button.grid(row=6, column=2)
        
        self.delete_button = tk.Button(self, text="Delete", command=self.delete_product, width=17)
        self.delete_button.grid(row=6, column=3)
        
    def create_product(self):
        name = self.name_entry.get()
        reference = self.reference_entry.get()
        count = self.count_entry.get()

        resultOfAdd = self.product.add(name, reference, count)
        
        print("resultOfAdd : ", resultOfAdd)
        
        if resultOfAdd:
            showMessage("SUCCESS", 
                            "\nProduct added successfully! \n")
        else:
            showMessage("ERROR", 
                        "\nSorry :( There is an error..\n")

    def read_products(self):
        resultOfGet = self.product.get_all()
        
        print("resultOfGet : ", resultOfGet)
        
        if resultOfGet:
            if len(resultOfGet) == 0:
                showMessage("WARNING", 
                        "\nSorry :( There is no product yet..\n")
            else:
                showWordsScreen(resultOfGet)
        else:
            showMessage("ERROR", 
                        "\nSorry :( There is an error..\n")
        
    def update_product(self):
        reference = self.reference_entry.get()
        count = self.count_entry.get()
        
        resultOfUpdate = self.product.update(count, reference)
        
        if resultOfUpdate:
            showMessage("SUCCESS", 
                            "\nProduct updated successfully! \n")
        else:
            showMessage("ERROR", 
                        "\nSorry :( There is an error..\n")
        
        print("resultOfUpdate : ", resultOfUpdate)
        
    def delete_product(self):
        reference = self.reference_entry.get()
        
        resultOfDelete = self.product.delete(reference)
        
        if resultOfDelete:
            showMessage("SUCCESS", 
                            "\nProduct deleted successfully! \n")
        else:
            showMessage("ERROR", 
                        "\nSorry :( There is an error..\n")
            
        print("resultOfDelete : ", resultOfDelete)
        
def main():
    app = ProductApp()
    app.mainloop()
    
main()
