import pytest


@pytest.mark.skip
class Example2:
    def Myclass(self):
        print("This is instance class...")
    @staticmethod
    def second(self,number):
        print(self,number)
obj1=Example2()
obj1.Myclass()
obj1.second(500,100)

class Example3:
    def m1(self,name):
        print("name is ",name)#instance
    @staticmethod
    def m2(self,job):
       print(self,job)
Exobj=Example3()
Exobj.m1(10)
Exobj.m2("Police","Railway")

