from datetime import *
class Person:
    today=date.today()
    def __init__(self,BornOn):
        self.BornOn=BornOn
    def Vote(self):
        self.age=self.today.year-self.BornOn.year-int((self.BornOn.month,self.BornOn.day)>(self.today.month,self.today.day))
        print(self.age)
        if self.age>=18:
            print('AWESOME!!...YOU ARE ELIGIBLE TO VOTE')
        else:
            print('OH NO!...YOU SHOULD STILL GROW UP TO VOTE!!')

print('enter your birth details:')
while(1):
    try:
        BornOn=date(int(input('enter year:')),int(input('enter month:')),int(input('enter day:')))
        P1 = Person(BornOn)
        P1.Vote()
    except:
        print('please enter valid date')
    a=input("Do you want to check again? Type 'y' if yes or type 'n' if u want to exit:")
    if a=='y':
        continue
    else:
        break
#P1=Person(BornOn)



