class Grandparent:
    height = 170
    satiety = 100
    age = 60

class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 50
    def __init__(self):
        print("height - ", self.height)
        print("age - ", self.age)
        print("satiety - ", self.satiety)

nick = Child()

class Wow:
    def __wow(self):
        print("Wow!!!")

    def _hello(self):
        print("hello")

some_obj = Wow()
some_obj._hello()

print()
some_obj._Wow__wow()
