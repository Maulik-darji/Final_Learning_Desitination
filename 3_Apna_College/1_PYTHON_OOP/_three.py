class Car:

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")


# class Toyota(Car):
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
    

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, brand, color, type):
        super().__init__(brand)
        self.type = type
        self.color = color

car1 = Fortuner("Toyota", "Black", "Diesel")
print("Brand: ", car1.brand)
print("Color: ",car1.color)
print("Type :", car1.type)

car1.start()
car1.stop()
# car1 = Toyota("Fortuner", "Black")
# car2 = Toyota("Prius", "White")

# print("Toyota Car 1:")
# car1.start()
# car1.stop()


# print("\nToyota Car 2:")
# car2.start()
# car2.stop()