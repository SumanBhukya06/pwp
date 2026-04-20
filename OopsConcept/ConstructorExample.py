class ConsExample:
    def __init__(self):
        print("This is constructor....")

    def m2(self):
        print("This is method..."+" "+"hello")
#invoke/Object creation
mc=ConsExample()
mc.m2()
#mc.m3(10,20)
# res=mc.m3(10,20)

#passing parameters

class PassPara:
    name = "joy"  # class
    def __init__(self,name):
        print("My local name is",name)
        print(self.name)
pp=PassPara("xo")



