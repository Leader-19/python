# color = ('red', 'blue', 'pink')

# converted = iter(color)
# print(next(converted))
# print(next(converted))
# print(next(converted))

#2

class Car:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")

class Boat:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")

class Plan:

    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Fly")

car = Car("BMW", "Sport")
boat = Boat("IBA", "Z19")
plan = Plan("Boing", "ZB200")

for x in (car, boat, plan):
    x.move()