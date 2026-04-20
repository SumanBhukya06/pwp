import pytest
@pytest.mark.skip
class Myclass:
    a,b=10,20#class variables
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)
#obj creation
mc=Myclass()
mc.add()
mc.mul()


i,j=100,200
@pytest.mark.skip
class Myclass1:
    c, d = 50, 60  # class variables
    def addition(self,x,y):#local variables
        print(x+y)
        print(self.c+self.d)
        print((i*j))#global variables

mc1=Myclass1()
mc1.addition(15,25)

#same variables
h,s=6,3#globals
class SameVariable:
    h,s=8,19#class
    def sameadd(self,h,s):
        print(h+s)#local
        print(self.h+self.s)
        print(globals()['h']+globals()['s'])
mc2=SameVariable()
mc2.sameadd(2,1)

#one class can have multiple objs
class Flower:
    def colour(self,color):
        print("The colour is: ",color)

obj=Flower()
obj.colour("red")

obj1=Flower()
obj1.colour("White")










