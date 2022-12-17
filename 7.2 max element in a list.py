class Number:
    def __init__(self):
        self.lst=[]
    def insert_element(self):
        self.lst.append(x)
    def Maximum(self):
        self.lst.sort()
        print("the maximum element is:",self.lst[len(self.lst)-1])


list1=Number()
while(1):
    x = int(input("enter a value:"))
    list1.insert_element()
    a=input("do u wish to add another element?:")
    if a=="n":
        break
    else:
        continue
list1.Maximum()


