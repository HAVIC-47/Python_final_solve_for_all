class Animel:
     def sound(self):
          return("Animel sound")
class humen(Animel):
     def speak(slef):
          return("kotha bole")
class cricketer(humen):
     def play(slef):
          return("cricketer play")
class bolwer(cricketer):
     def bowl(slef):
          return("bolwer bowl")
class batsman(cricketer):
     def bat(slef):
          return("batsman bat")
class allrounder(bolwer,batsman):
     def allround(slef):
          return("can bat and bowl")

all_rounder = allrounder()
print(all_rounder.sound())  # Inherited from Animal
print(all_rounder.speak())  # Inherited from Human
print(all_rounder.play())   # Inherited from Cricketer
print(all_rounder.bowl())   # Inherited from Bowler
print(all_rounder.bat())    # Inherited from Batter
print(all_rounder.allround())  # Specific to AllRounder
