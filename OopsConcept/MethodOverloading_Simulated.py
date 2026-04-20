class Human:
    def sayHi(self,name=None):
        if name is not None:
            print("hello"+name)
        else:
            print("Hello")
h=Human()
h.sayHi()
h.sayHi("Joy")