class Cal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    #adding
    def add(self):
        return (self.a+self.b)
    #subtracting
    def sub(self):
        return (self.a-self.b)
    #multiplication
    def mul(self):
        return (self.a*self.b)
    #division
    def div(self):
        return (self.a/self.b)

a=int(input('enter first number: '))
b=int(input('enter second number'))
obj=Cal(a,b)

choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. subtract")
    print("3. Multiply")
    print("4. Divide")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("Result: ",obj.add())

    elif choice==2:
        print("Result ",obj.sub())

    elif choice==3:
        print("Result: ",obj.mul())

    elif choice==4:
        print("Result: ",obj.div())

    elif choice==0:
        print("Existing...")

    else:
        print("Invalid choice..")

print()