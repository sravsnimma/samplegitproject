''' 1.single inheritance
    2.multilevel inheritance
    3.heirarical inheritance
    4.multiple inheritance
    '''
 #single inheritance example
# class Parent:
#     def fun1(self):
#      print('this is parent class')
# class Child(Parent):
#     def fun2(self):
#      print('this is child class')    
# obj=Child()
# obj.fun1()
#---------------------------------
 #multilevel inheritance example
# class Parent:
#     def pfun(self):
#      print('this is parent class')
# class Child(Parent):
#     def cfun(self):
#      print('this is child class')   
# class GrandChild(Child):
#     def gcfun(self):
#      print('this is grandchild class')     
# obj=GrandChild()
# obj.pfun()
# obj.cfun()
# obj.gcfun()
#---------------------------------
#multiple inheritance
# class ParentC:
#     def Pfunc(self):
#         print('this is Parent')
# class Parent2C:
#     def P2fun(self):
#         print('this is parent2')  
# class ChildC(ParentC,Parent2C):
#     def cfun(self):   
#         print('this is child')     
# obj=ChildC()
# obj.Pfunc()
# obj.P2fun()        
#--------------------------------
#heirarical inheritance
class ParentCl:
    def funP(self):
        print('this is parentclass')
class Child1(ParentCl):
    def funC1(self):
        print('this is child 1 class')
class Child2(ParentCl):
    def funC2(self):
        print('this is child 2 class')        
obj1=Child1()
obj=Child2()
obj.funC2()
obj.funP()
obj1.funC1()        