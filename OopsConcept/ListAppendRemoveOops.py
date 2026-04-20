class check:
    def __init__(self):
        self.n=[]
    def append(self,a):
         self.n.append(a)
    def remove(self,b):
        if b in self.n:
            self.n.remove(b)
        else:
            print("Element not found")
    def dis(self):
        return self.n
obj=check()
choice =1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Remove")
    print("3. Multiply")
    print("4. Divide")
    choice=int(input("Enter your choice: "))
    if choice==1:
        n=int(input("Enter number to append: "))
        obj.append(n)
        print("List: ",obj.dis())
    elif choice==2:
        n=int(input("Enter number to remove: "))
        obj.remove(n)
        print("List: ",obj.dis())

    elif choice==3:
        print("List: ",obj.dis())

    elif choice==0:
        print("Existing...")

    else:
        print("Invalid choice..")
print()