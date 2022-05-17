class Human:
    height = 170
    satiety = 50

class Student(Human):
    pass
    #satiety = 0

class Worker(Human):
    #pass
    satiety = 100

nick = Student()
ann = Worker()

print("Nick - ", nick.height)
print("Ann - ", ann.height)
print("Nick - ", nick.satiety)
print("Ann - ", ann.satiety)

