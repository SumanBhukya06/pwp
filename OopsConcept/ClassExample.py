class Emp:
    name="joy"
    id=7
    salary=20000
    address="BLR"
#constructor
    def __init__(self,ename,eid,esal,eaddress):
        self.ename=ename
        self.eid=eid
        self.esal=esal
        self.eaddress=eaddress

#Method
    def display(self):
        print(self.ename,self.eid,self.esal,self.eaddress)
        print(self.name,self.id,self.salary,self.address)

    def __str__(self):
        return (self.ename,self.eaddress)
        #return (self.name,self.salary)

emp=Emp("Maya",8,10000,"Hyd")
emp.display()
#print(emp)


