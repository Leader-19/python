#python oop
# class Car:
#     x = 5

# car = Car()
# print(car.x)

# class Car:
#     def __init__(self) -> None:
#         print("First run")

# car = Car()
#2
# class Car:
#     def __init__(self, name, brand) -> None:
#         self.name = name
#         self.brand = brand

# car = Car("GTR", "light style")
# print(car.brand)
# print(car.name)

# #3
# class Car:
#     def __init__(self, name, brand) -> None:
#         self.name = name
#         self.brand = brand
#     def __str__(self) -> str:
#         return f"{self.brand}"

# car = Car("GTR", "light style")
# print(car.brand)

#4
# class Car:

#     myProperty = 10

#     def __init__(self, name, brand) -> None:
#         self.name = name
#         self.brand = brand
#     def __str__(self) -> str:
#         return f"{self.brand} {self.name}"
    
#     def calculate(self, a, b):
#         return a + b + self.myProperty

# car = Car("GTR", "light style")
# # print(car)

# cal = car.calculate(10, 20)
# print(cal)
#5

class Car:
    myPreperty = 10
car = Car()
car.myPreperty = 30
print(car.myPreperty)