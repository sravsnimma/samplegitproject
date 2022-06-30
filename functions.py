def firstFunction():
    print('first function program')
firstFunction()
def add(a,b):
    return a+b
c=add(1,2)    
print(c)

def orbitfun(*x):
    return x
s=orbitfun(1,2,3,4,5)#it returns it as a tuple (1,2,3,4)
print(s)

def keyfun(**n):
    return n
m=keyfun(name='sravanthi',age=21)#it returns a dictionary {'name'='sra','age'=0}
print(m)    
