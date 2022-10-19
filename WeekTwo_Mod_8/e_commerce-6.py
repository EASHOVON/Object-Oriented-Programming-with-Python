
class Shopper:
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self,item,price,quantity):
        self.cart.append({"item":item,"price":price,"quantity":quantity})

    def checkout(self,ammount):
        price = 0
        for item in self.cart:
            price += item['price'] * item['quantity']
        if price > ammount:
            return f'Please Give me more money: {price-ammount} and take your item.'
        elif price < ammount:
            return f'Take your remaining money: {ammount-price} and take your item'
        else:
            return "Here is your item"

shopper = Shopper("Bag Tan")

shopper.add_to_cart("T-shirt",800,8)
shopper.add_to_cart("Pant",550,5)
shopper.add_to_cart("Shoes", 860,9)

reply = shopper.checkout(2000)
print(reply)