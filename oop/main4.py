class Paratent:
    def __init__(self, name) -> None:
        self.name = name

    def printName(self):
        print(self.name)

class Child(Paratent):
    def __init__(self, name, age) -> None:
        super().__init__(self, name)

child = Child("Leader Din", 19)
child.printName()