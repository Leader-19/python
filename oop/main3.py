class Paratent:
    def __init__(self, name) -> None:
        self.name = name

class Child(Paratent):
    def __init__(self, name, age) -> None:
        self.name = name
child = Child("Leader Din", 19)
print(child.name)