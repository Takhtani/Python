# 1. Single inheritance
class Parent:
    def show_parent(self):
        print("This is the Parent class")
class Child(Parent):
    def show_child(self):
        print("This is the Child class")

# 2. Multiple inheritance
class Father:
    def skills(self):
        print("Father: gardening")
class Mother:
    def talent(self):
        print("Mother: painting")
class Son(Father, Mother):
    pass

# 3. Multilevel inheritance
class Grandfather:
    def house(self):
        print("Grandfather: owns a house")
class Dad(Grandfather):
    def car(self):
        print("Dad: owns a car")
class Kid(Dad):
    def bike(self):
        print("Kid: owns a bike")

# 4. Hierarchical inheritance
class Vehicle:
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass

# 5. Hybrid inheritance (diamond shape)
class A:
    def who(self):
        print("Class A")
class B(A):
    pass
class C(A):
    def who(self):
        print("Class C")
class D(B, C):
    pass

print("--- Single ---")
c = Child(); c.show_parent(); c.show_child()
print("--- Multiple ---")
s = Son(); s.skills(); s.talent()
print("--- Multilevel ---")
k = Kid(); k.house(); k.car(); k.bike()
print("--- Hierarchical ---")
Car().start(); Bike().start()
print("--- Hybrid ---")
D().who()
print("Method Resolution Order of D:", [cls.__name__ for cls in D.mro()])
