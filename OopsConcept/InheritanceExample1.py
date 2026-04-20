import pytest


@pytest.mark.skip(reason="this is a test")
class A:
    def m1(self):
        print("This is method from class A")
class B(A):
    def m2(self):
        print("This is method from class B")

bobj=B()
bobj.m1()
bobj.m2()
#single level inheritance
#a,b=6,5
class x:
    def __init__(self,c,d):
        self.c=c
        self.d=d

    #c,d=100,200
    def f1(self):
        print("This is from class A: ",self.c*self.d)
        #print(a+b)

class y(x):
    #h,s=50,60
    def f2(self):
        print("This is from class B: ",self.c+self.d)

yobj=y(50,125)
yobj.f1()
yobj.f2()
