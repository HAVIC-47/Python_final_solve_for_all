# dada
class gari():
     def __init__(self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
     def sound(self):
        print("Vroom Vroom")
# baba
class four_Wheeler(gari):
     def __init__(self, brand, model, year, horsepower):
          super().__init__(brand, model, year)
          self.horsepower = horsepower        

     def has_turbo(self):
          print(" four wheeler has turbo")
# chacha
class two_Wheeler(gari):
     def __init__(self, brand, model, year, horsepower, type):
         super().__init__(brand, model, year)
         self.horsepower = horsepower
         self.type = type

     def has_ABS(self):
           print(" two wheeler has ABS")
# ami
class sports_car(four_Wheeler):
     def __init__(self, brand,model,year,horsepower, door_type):
          super().__init__(brand,model,year,horsepower)
          self.door_type = door_type

     def door_count(self):
          print("door count is 2")
# amar bou    
class exotic_car():
     def __init__(self, exclusivity):
          # super().__init__(brand, model, year)
          self.exclusivity = exclusivity

     def is_exclusive(self):
          print("this car is exclusive")
# amar baccha
class hyper_car(sports_car,exotic_car):
     def __init__(self, brand,model,year,horsepower,door_type,exclusivity, top_speed):
          sports_car.__init__(self,brand,model,year,horsepower,door_type) 
          exotic_car.__init__(self,exclusivity)
          self.top_speed = top_speed

     def is_hyper(self):
          print("this car is hyper")


car1 = hyper_car("Bugatti","Chiron",2021,1500,"scissor doors",500, 261)
car1.sound()
car1.has_turbo()
car1.door_count()
car1.is_exclusive()
car1.is_hyper()
print(car1.brand)
print(car1.model)
print(car1.year)
print(car1.horsepower)
