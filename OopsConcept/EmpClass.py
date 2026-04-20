class Employee:
    def __init__(self,eid,ename,esal):
        self.eid=eid  #here eid is the local variable accessing from class variable
        self.ename=ename
        self.esal=esal
    def display(self):
        print(self.eid,self.ename,self.esal)

emp=Employee(100,"joy",50000)
emp.display()

# example 10
class Doctor:
    def __init__(self,dId,dname,djob,dsal):
        self.dId=dId
        self.dname=dname
        self.djob=djob
        self.dsal=dsal
#return string data
    def __str__(self):
        return (self.dname)
doc=Doctor(200,"joy","ortho",25000)
print(doc)
