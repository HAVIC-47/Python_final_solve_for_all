def combination(n,r):
     if r==0 or r==n :
          return 1
     else:
          return combination(n-1 ,r-1)+combination(n-1 ,r)
     

n,r= 5,2
print(f"combination c{n},{r} = {combination (n,r)}")



def permutation(n,r):
     if r==0:
          return 1
     else:
          return n*permutation(n-1,r-1)
     
n,r= 5,2
print(f"Permutation P({n}, {r}) = {permutation(n, r)}")
