from abc import ABC , abstractmethod

class car(ABC):
    
     @abstractmethod
     def brand(self):
          pass
    
     @abstractmethod
     def model(self):
          pass
    
class notun_gari(car):
     def door_count(self):
          print("door count is 2")

     def brand(self):
          print("Brand: BMW")
     
     def model(self):
          print("M3 compitition")

amar_gari = notun_gari()
amar_gari.brand()
amar_gari.model()
amar_gari.door_count()