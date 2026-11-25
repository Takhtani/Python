class Animal:
    def sound(self):
        print("Animal makes a sound")

    def move(self):
        print("Animal moves")

class Dog(Animal):
    def sound(self):                 # overrides Animal.sound()
        print("Dog barks: Woof! Woof!")

    def show_parent_sound(self):
        super().sound()              # calling the parent version

a = Animal()
d = Dog()

print("Animal object:")
a.sound()
print("Dog object:")
d.sound()
d.move()                             # inherited, not overridden
print("Parent method using super():")
d.show_parent_sound()
