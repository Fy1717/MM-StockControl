from database import Database
from product import Product

def main():
    db = None
    
    try:
        db = Database("D://mydatabase.db")

        print("\nConnected To Database")
            
        product = Product(db)
        product.create_table()
        
        if product:
            print("\nConnected To Products")
            
            while True:
                print("\n1. Show all products")
                print("2. Add a product")
                print("3. Update a product")
                print("4. Delete a product")
                print("5. Exit")
                
                choice = input("\nEnter your choice: ")

                if choice == "1":
                    products = product.get_all()
                    
                    if len(products) == 0:
                        print("\nÜRÜN LİSTESİ BOŞ..")
                    else:
                        print("\n#--------------------------------------------------------#")
                        
                        for p in products:
                            print("\nID : ", p[0], "\nNAME : ", p[1] ,"\nREFERENCE : ", p[2],"\nCOUNT : ",p[3])
                            
                        print("\n#--------------------------------------------------------#\n")
                elif choice == "2":
                    name = input("\nEnter product name: ")
                    reference = input("Enter product reference: ")
                    count = int(input("Enter product count: "))
                    
                    processResult = product.add(name, reference, count)
                                
                    if processResult:
                        print("\nProduct added successfully!")
                    else:
                        print("\nSorry :( There is a problem..")
                elif choice == "3":
                    id = int(input("\nEnter product id: "))
                    
                    isThereProduct = product.get(id)
                    
                    if isThereProduct:
                        count = int(input("\nEnter new product count: "))
                        
                        processResult = product.update(count, id)
                        
                        if processResult:
                            print("\nProduct updated successfully!")
                        else:
                            print("\nSorry :( There is a problem..")
                    else:
                        print("\nSorry :( I couldnt found this product..")
                elif choice == "4":
                    id = int(input("\nEnter product id: "))
                    
                    isThereProduct = product.get(id)
                    
                    if isThereProduct:
                        processResult = product.delete(id)
                        
                        if processResult:
                            print("\nProduct deleted successfully!")
                        else:
                            print("\nSorry :( There is a problem..")
                    else:
                        print("\nSorry :( I couldnt found this product..")
                elif choice == "5":
                    print("\nExiting...")
                    
                    break
                else:
                    print("\nInvalid choice. Please try again.")
        else:
            print("\nSorry :( There is an error for connecting to products..")
    except:
        print("\nSorry :( There is an error for connecting to database..")
main()