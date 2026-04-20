class C:
    a,b=10,20
    def m1(self):
        print("This is c class",self.a+self.b)
class C1:
    x,y=30,40
    def m2(self):
        print("This is C1 class: ",self.x+self.y)
class P(C,C1):
    def m3(self):
        print("This is P class ")

pobj=P()
pobj.m1()
pobj.m2()
pobj.m3()
