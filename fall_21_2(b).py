import math

class Cylinder:
     def __init__(self, radius, height):
          self.radius = radius
          self.height = height
     def surface_area(self):
          return 2*math.pi*self.radius*(self.radius+self.height)
     
     def volume(self):
          return math.pi*self.radius**2*self.height
     
biri=Cylinder(3,5)
print(biri.surface_area())
print(biri.volume())