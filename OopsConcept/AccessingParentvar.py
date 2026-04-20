class A:
    a,b=10,50#parent class variables
class B(A):
    i,j=45,60#child class variables
    def m1(self,x,y):
        print(x+y)
        print(self.i+self.j)
        print(self.a+self.b)
bobj=B()
bobj.m1(85,95)


