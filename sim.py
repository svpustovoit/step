import random
class Human:
 def __init__(self, name="Human", job=None,  home=None, car=None):
   self.name = name
   self.money = 100
   self.gladness = 50
   self.satiety = 50
   self.job = job
   self.car = car
   self.home = home
 def get_home(self):
    self.home = House()
 def get_car(self):
   self.car = Auto(brands_of_car)
 def get_job(self):
    if self.car.drive():
      pass
    else:
      self.to_repair()
      return
    self.job = Job(job_list)
def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
        return
        self.satiety += 5
        self.home.food -= 5

        def work(self):
            if self.car.drive():
                pass
            else:
                if self.car.fuel < 20:
                   self.shopping("fuel")
                   return
                else:
                  self.to_repair()
                  return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
 def shopping(self, manage):
    if self.car.drive():
        pass
    else:
        if self.car.fuel < 20:
            manage = "fuel"
        else:
            self.to_repair()
        return
    if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
    elif manage == "food":
        print("Bought food")
        self.money -= 50
        self.home.food += 50
    elif manage == "delicacies":
        print("Hooray! Delicious!")
        self.gladness += 10
        self.satiety += 2
        self.money -= 15
 def chill(self):
    self.gladness += 10
    self.home.mess += 5
 def clean_home(self):
    self.gladness -= 5
    self.home.mess = 0
 def to_repair(self):
        self.car.strength += 100

        self.money -= 50

 def days_indexes(self, day):
    day = f" Today the {day} of {self.name} 's life "
    print(f"{day:=^50}", "\n")
    human_indexes = self.name + "'s indexes"
    print(f"{human_indexes:^50}", "\n")
    print(f"Money – {self.money}")
    print(f"Satiety – {self.satiety}")
    print(f"Gladness – {self.gladness}")
    home_indexes = "Home indexes"
    print(f"{home_indexes:^50}", "\n")
    print(f"Food – {self.home.food}")
    print(f"Mess – {self.home.mess}")
    car_indexes = f"{self.car.brand} car indexes"
    print(f"{car_indexes:^50}", "\n")
    print(f"Fuel – {self.car.fuel}")
    print(f"Strength – {self.car.strength}")