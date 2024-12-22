import cmath
def equition(a,b,c):
     discriminant = cmath.sqrt(b**2) - (4*a*c)
     root1=(-b + discriminant)/(2*a)
     root2=(-b - discriminant)/(2*a)

     print(f"the solution are {root1} and {root2}")

equition(1 ,-3, 2)
