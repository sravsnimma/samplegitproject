class demo1:
    def __init__(self):
     print('indentatioin is very very important in python!!!!')
    def fundemo(self):
     print('method')    
o=demo1()
o.fundemo()    
class demo:
    def __init__(self,a,b,c) :
        self.a=a
        self.b=b
        self.c=c
    def display(self):
        print(self.a)  
        print(self.b)  
        print(self.c)    
        if self.a>self.b and self.a>self.c:
         print('a is greter than b & c')    
        elif self.b>self.a and self.b>self.c:
         print('b is greter than a & c')    
        else:
         print('c is greter than a &b')    
objt=demo(10,12,20)        
objt.display()