class Animel:
     def __init__(self,name):
          self.name = name

class Mammal(Animel):
     def __init__(self, name,water_being):
          super().__init__(name)
          self.water_being = water_being

class WaterAnimal(Mammal):
     def __init__(self,name,water_being,swim_speed):
          super().__init__(name,water_being)
          self.swim_speed = swim_speed

     def sound(self):
          return "sound"

class shark(WaterAnimal):
     def __init__(self, name, water_being, swim_speed):
          super().__init__(name, water_being, swim_speed)

     def sound(self):
          return "grrrrrr"