class Phone:
    manufactured = "China"
    
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color

my_phone = Phone("Xaomi",38000,"Green")
print(my_phone.brand)

her_phone = Phone("Huwei",25000,"Golden")
print(her_phone.brand)

dad_phone = Phone("Samsung",12000,"Black")
print(dad_phone.brand)