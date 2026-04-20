class S:
    def m1(self):
        print("This is m1 method..")
class J(S):
    def m2(self):
        print("This is child class..")
        #super().m1()


class F(J):
    def m3(self):
        super().m2()
cobj=F()
#cobj.m1()
cobj.m3()