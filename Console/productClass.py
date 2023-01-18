class Product:
    def __init__(self, name, referance, count):
        self.name = name
        self.referance = referance
        self.count = count
           
    def updateProductCount(self, newCount):
        if type(newCount) is int:
            if newCount >= 0:
                self.count = newCount
            else:
                print("Negatif sayida ürün olamaz!")
        else:
            print("Lütfen sayı giriniz")
          