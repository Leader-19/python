class Parent:
    x = 10
    def test(self):
        return "Hello"
# parent = Parent()
# print(parent.x)
class Child(Parent):
    pass
child = Child()
print(child.test())