class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):                   # single inheritance
    def bark(self):
        print(f"{self.name} says Woof! Woof!")

d = Dog("Tommy")
d.eat()                              # inherited from Animal
d.bark()                             # defined in Dog
print("Is Dog a subclass of Animal?", issubclass(Dog, Animal))
