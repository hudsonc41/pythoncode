class Shop:
    def __init__(self, name):
        self.name = name

    def buy(self, item, price):
        return f"You bought {item} for ${price}."


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price(self):
        return self.price


class Animal:
    def __init__(self, name, species_name):
        self.name = name
        self.species_name = species.name


class Pet(Animal):
    def __init__(self, owner):
        self.owner = owner


class Dog(Pet):
    def bark(self):
        print(f"{self.name} barks")


line = input("")
while line:
    if line.lower() == "dog":
        dog = input("Dog: ")
        dog = Dog()
    if line.lower() == "buy" or line.lower() == "shop":
        shop_name = input("Shop: ")
        shop = Shop(shop_name)
        item_info = input("Item, price: ").split()
        item = Item(item_info[0], item_info[1])
        purchase = shop.buy(item.name, item.price)
    line = input("")
