#age=20
# print("I am",age,"years old")

# def a(age):
#     print("I am",age,"years old")
# a(20)
# age=20
# def b():
#     print("I am",age,"years old")
# b()


#using constructor
class Person:
    def __init__(self,age):
        self.age=age
    def b(self):
        print("I am",self.age,"years old")
obj = Person(20)
obj.b()

