class H:
    def __init__(self,x="Hello",y="Maya"):
        self.x=x
        self.y=y
    def display(self):
        print(self.x,self.y)
class I(H):
    a,b=11,21
    def m2(self):
        print(self.a,self.b)

class J(I):
    m,n=10,20
    def m1(self):
        print(self.m,self.n)

iobj=I()
iobj.display()
iobj.m2()

jobj=J()
jobj.display()
jobj.m1()


