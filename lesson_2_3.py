class Student:
    amount_of_students = 0
    def __init__(self, height=160):
        self.height = height
        Student.amount_of_students += 1

    def grow(self, height=1):
        self.height += height

nick = Student()
kate = Student(height=170)

nick.grow(height=15)
kate.grow(height=10)
print(nick.height)
print(kate.height)
