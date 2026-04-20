class Parent:
    name="Joy"
    sal=52000
    address="BLR"

class Child(Parent):
    name = "Maya" #overriding variable
    sal=25000
    address="HYD"

cobj=Child()
print(cobj.name,cobj.sal,cobj.address)