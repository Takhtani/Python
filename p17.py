class Laptop:
    def __init__(self, brand):
        self.brand = brand
        self.cpu = self.CPU("Intel i5", 4)     # object of inner class

    def show(self):
        print("Laptop brand:", self.brand)
        self.cpu.show()

    class CPU:                                  # inner class
        def __init__(self, name, cores):
            self.name = name
            self.cores = cores

        def show(self):
            print(f"CPU: {self.name} with {self.cores} cores")

lap = Laptop("Dell")
lap.show()

# creating an object of the inner class directly
cpu2 = Laptop.CPU("AMD Ryzen 7", 8)
cpu2.show()
