class Animal:
    def __init__(self, species):
        self.species = species


class Pet(Animal):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def pet(self):
        print(f"{self.name} is pet")


class Cat(Pet):
    def meow(self):
        print(f"{self.name} meows")


class Dog(Pet):
    def bark(self):
        print(f"{self.name} barks")


name = input("What is the dog's name? ")
owner = input("Who is there owner? ")
neighbour_dog = Dog(name, owner)
neighbour_dog.bark()
