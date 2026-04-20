class A:
    def __init__(self,h="high",s="school"):
        self.h=h
        self.s=s
    def school(self):
            print(self.h,self.s)
    c,d=14,16
    def a1(self):
        print(self.c+self.d)

class B(A):
    x,y=5,6
    def b1(self):
        print(self.x+self.y)

class C(B):
    i,j=9,10
    def c1(self):
        print(self.i%self.j)

cobj=C()
cobj.a1()
cobj.school()
cobj.b1()
cobj.c1()