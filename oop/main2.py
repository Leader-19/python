class Paratent:
    def __init__(self, name) -> None:
        self.name = name

class Child(Paratent):
    pass
child = Child("Leader Din")
print(child.name)