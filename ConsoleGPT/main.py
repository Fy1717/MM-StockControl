from database import Database
from product import Product

def main():
    db = Database("D://FY-Home//mydatabase.db")
    product = Product(db)
    product.create_table()

    while True:
        print("\n1. Show all products")
        print("2. Add a product")
        print("3. Update a product")
        print("4. Delete a product")
        print("5. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            products = product.get_all()
            for p in products:
                print("\nÜrün İd'si : ", p[0], "\nÜrün Adı : ", p[1] ,"\nÜrün Referansı : ", p[2],"\nÜrün Adedi : ",p[3])
        elif choice == "2":
            name = input("Enter product name: ")
            reference = input("Enter product reference: ")
            count = int(input("Enter product count: "))
            product.add(name, reference, count)
            print("Product added successfully!")
        elif choice == "3":
            id = int(input("Enter product id: "))
            count = int(input("Enter new product count: "))
            product.update(count, id)
            print("Product updated successfully!")
        elif choice == "4":
            id = int(input("Enter product id: "))
            product.delete(id)
            print("Product deleted successfully!")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()