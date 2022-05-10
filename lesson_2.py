class Student:
    amount_of_students = 0
    def __init__(self, height=160):
        self.height = height
        print('I am alive!')
        Student.amount_of_students += 1

first_student = Student()
#Student.__init__(self=first_student)

nick = Student()
print(nick.height)

jane = Student()
print(jane.height)

kate = Student(height=170)
print(kate.height)

print(nick.amount_of_students)
print(Student.amount_of_students)

