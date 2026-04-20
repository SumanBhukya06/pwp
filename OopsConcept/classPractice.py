class Person:#class
    def my_self(self):#method self default
        print("I am my self")
    def my_other(self):
        print("I am my other")
    def first(self):
        print("this is first")
    def second(self):
        print("this is second")
    def third(self):
        print("this is third")
    def name(self,Name,Id,Sal,Job):
        print("My name is: ",Name)
        print("My id is: ",Id)
        print("My sal is: ",Sal)
        print("My job is: ",Job)

#object
ms=Person()
ms1=Person()
ms.my_self()
ms1.my_other()
firstobj=Person()
firstobj.first()
secondobj=Person()
secondobj.second()
thirdobj=Person()
thirdobj.third()
nobj=Person()
nobj.name("Joy",7,5000,"SWE")
