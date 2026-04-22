def creating_str_double():
    name="Joy"#double quotes
    grade="A"
    #return name,grade
    return name+grade
print(creating_str_double())
print(type(creating_str_double()))

def creating_str_single():
    name="maya"
    grade="A+"
    s=name+grade
    return s
print(creating_str_single())
#str operations
def str_op():
    name="Kai"
    grade="B+"
    place="Blr"
    return name+grade+place
print("*"*10)
print(str_op())

def str_op2(name="Joy",grade="C",place="Hyd"):
    return name," "+grade," "+place," "
print(str_op2())
#slicing strings
def slicing_str(s):
    print(s[1:3])#el starts from zero
    print(s[:5])#Welco
    print(s[-3:-1])
slicing_str("Welcome")
#rev a string
def rev_str():
    q="Joy"
    rev=""
    for i in q:
        rev=i+rev
        print(rev)
rev_str()

#formatting strings
def formatting_str():
    price=100
    print(f'The price is:{price}')
    print(f'The price is:{price} USD')
    print(f'The price is:{price:.2f}')

formatting_str()

#membership op
def mem_op(u):
    print("Eu" in u)#True
    print("x" in u)#False
    print("y" not in u)#True
mem_op("Europe")

#String a immutable means we can change the previous value
def str(k,l):
    print(k[0])
    #k[0]="K"
    l="M"+k[1:]
    print(l)

str("Levis","Love")

def lst():
    lst=['s','l','o','w']
    lst[0]="P"
    print(lst)
lst()

#len()
def str_len():
    person="Doctor"
    print(len(person))
str_len()
'''
capitalize(
casefold()
upper()
lower()
title()
swapcase()
'''
def str_methods():
    breed="bulldog"
    print(breed.capitalize())
    print(breed.casefold())
    print(breed.upper())
    print(breed.lower())
    print(breed.title())
    print(breed.swapcase())

str_methods()

#alignment and formatting
def align_for():
    print("Hello".center(6,'*'))
    print("Hello,{}!".format("Joy"))

align_for()

#search and find
def search_find():
    h="world!!"
    print(h.find("w"))
    print(h.index("r"))

search_find()
#count and replace
def count_rep():
    s='apple'
    # print(s.count('p'))
    count=0
    ch='p'
    for c in s:
        if c==ch:
            count+=1
    print("The count is:",count)
count_rep()

#validation(boolean checks)
def val():
    print("abc123".isalnum())
    print("Hello".isalpha())
    print("hello".islower())
    print("HELLO".isupper())
val()

def split():
    s="one,two,three"
    print(s.split(","))
split()















