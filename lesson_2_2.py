class Student:
    '''height = 160
    def __init__(self):
        print(self.height)
        self.height+=10'''

    def __init__(self):
        self.height = 170
    height = 160
    def printer(self):
        print(self.height)

nick = Student()
kate = Student()
nick.printer()
kate.printer()
