class bap:
     def __init__(self, bap_nam, bap_boyosh):
         self.bap_nam = bap_nam
         self.bap_boyosh = bap_boyosh

     def bap_boka_Dey(self):
          return f"{self.bap_nam} byoush {self.bap_boyosh} onek boka dey"

class ammu:
     def __init__(self, ma_nam):
          self.ma_nam = ma_nam

     def ma_boka_Dey(self):
          return f"{self.ma_nam} boka dey na"
     
class ami(bap, ammu):
     def __init__(self, bap_nam,bap_boyosh, ma_nam, amar_nam ):
          bap.__init__(self, bap_nam,bap_boyosh)
          ammu.__init__(self, ma_nam)
          self.amar_nam = amar_nam

     def boka_khai(self):
          return f"{self.amar_nam} boka khai"
     
ami_ke= ami("amar bap", "72","amar ma", "amar nam")

print(ami_ke.boka_khai())
print(ami_ke.ma_boka_Dey())
print(ami_ke.bap_boka_Dey())
     