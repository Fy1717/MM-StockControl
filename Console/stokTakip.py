from productClass import Product

productList = []

def listAllProducts():
    if len(productList) == 0:
        print("\nÜrün listesi boş..")
    else:    
        print("\n\n========================= ÜRÜN LİSTESİ ===================================\n")
        
        for product in productList:
            print(" # İsim : ", product.name, " - Referans : ", product.referance, " - Sayı : ", product.count)
            
        print("\n==========================================================================\n\n")
            
def createProduct():
    try:
        name = input("\n --> Ürün ismi giriniz : ")
        reference = input(" --> Referans kodunu giriniz : ")
        count = int(input(" --> Ürün adedini giriniz : "))
        
        product = Product(name, reference, count)    
        
        productList.append(product)
        
        listAllProducts() 
    except:
        print("\nÜrün oluşturulurken hata! Yeniden deneyin.")
    
def updateProduct():
    if len(productList) == 0:
        print("\nÜrün listesi boş..")
    else:        
        listAllProducts()
            
        selectedProductReference = input("\n\n --> Güncellemek istediğiniz ürünün referansı : ")
        
        selectedProduct = None
        for product in productList:
            if product.referance == selectedProductReference:
                selectedProduct = product            

        if selectedProduct is not None:
            print("\n\n==============================\n\nGÜNCELLENECEK ÜRÜN : \n-------------------------\n\nİsim = ", selectedProduct.name, "\nReferans = ", selectedProduct.referance, "\nÜrün sayısı = ", selectedProduct.count, "\n\n==============================\n\n")
            
            try:
                newCount = int(input("\n --> Yeni ürün sayısını girin : "))
                
                selectedProduct.updateProductCount(newCount)
                
                print("\n ", selectedProduct.name, " isimli ürün sayısı güncellendi!")
                
                listAllProducts()                
            except:
                print("\nHatalı girdi yaptınız!")
        else:
            print("\nAranılan ürün stokta bulunamadı..")
                  
def removeProduct():
    listAllProducts()
    
    if len(productList) != 0:
        try:
            selectedProductReference = input("\n --> Silmek istediğiniz ürünün referans kodunu giriniz : ")
            
            deletedProductIndex = None
            for index in range(0, len(productList)):
                if selectedProductReference == productList[index].referance:
                    deletedProductIndex = index
                    
                    break
                    
            if deletedProductIndex is not None:
                productList.pop(deletedProductIndex)
                
                print("\n ", selectedProductReference, " referanslı ürün silindi!")
            else:
                print("\n Ürün listede bulunamadı!")
        except Exception as e:
            print("\n Hata oluştu! ", str(e))
            
while True: 
    try:
        islemCode = int(input("\n==============================\n\n - Ürünleri Listele : 1\n - Yeni ürün oluştur : 2\n - Ürün sayısını güncelle : 3\n - Ürünü sil : 4\n\n==============================\n\n --> Yapmak istediğiniz işlemi seçin : "))

        if islemCode == 1:
            listAllProducts()
        elif islemCode == 2:
            createProduct()
        elif islemCode == 3:
            updateProduct()
        elif islemCode == 4:
            removeProduct()
        else:
            print("\nDaha fonksiyonunu yazmadık dayı :D")
    except:
        print("\nYanlış seçenek..")