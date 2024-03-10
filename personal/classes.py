class Dog:

    def __init__(self, name):
        self.name = name

    def add_1(self, x):
        return x + 5

    def bark(self):
        print("bark")

    def get_name(self):
        return self.name


d = Dog("Tim")
print(d.get_name())
print(d.name)
d.bark()
print(d.add_1(5))
print(type(d))
