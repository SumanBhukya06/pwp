'''
ordered
changeable(mutable)
Duplicate values allowed
[]-represent
'''
class lsr:
    mylist=[10,20,30,40,50]
    mylist2=['apple','cherry','guava','kiwi']
    mylist3=[2,5,'watermelon','papaya']#mixed data types
    def creating_lst(self):
        print(self.mylist)
        print(self.mylist2)
        print(self.mylist3)
        print(self.mylist[0])#10 accessing items
        print(self.mylist2[3])#accessing items
        print(self.mylist3[3])#accessing items
        print(self.mylist2[-1])#accessing items
        #range of indexes
        print(self.mylist2[1:3])
        print(self.mylist3[-3:-1])

        #changing item value
        self.mylist[1]="beetroot"
        self.mylist2[0]=100
        print(self.mylist)
        print(self.mylist2)

        #loop through a list
        # for item in self.mylist:
            #print(item)
        if "beetroot" in self.mylist:
            print("yes present")
        #list functions
        print(len(self.mylist3))
        print(self.mylist3.count('papaya'))

        #sorting and reversing
        # self.mylist2.sort()
        # print(self.mylist2)

        #adding items
        self.mylist2.append("ice apple")#append add at end
        self.mylist2.insert(1,"Orange")#specific position
        print(self.mylist2)

        #removing item
        self.mylist2.remove("kiwi")#removing by value
        # self.mylist2.pop(0)#by index
        # del self.mylist2[0]#delete specific item
        # self.mylist2.clear()#clears all items
        print(self.mylist2)

        #copying a list
        self.mylist2=self.mylist.copy()
        print(self.mylist2)

        #joining lists + and extend()
        print(self.mylist+self.mylist3)

        self.mylist3.extend(self.mylist2)
        print(self.mylist3)


obj=lsr()
obj.creating_lst()

