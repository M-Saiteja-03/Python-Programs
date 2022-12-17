#WAP that has a class Student that stores roll, name and marks(3 subjects) of the students.
#Display the information of the student with his/her percentage
class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def marks(self,OOPS,MATH,CHEM,I4):
        self.sub1=OOPS
        self.sub2=MATH
        self.sub3=CHEM
        self.sub4=I4
        print(f'name:{self.name}\nrollno:{self.roll}')
        print("marks:")
        print(f"OOPS:{self.sub1}\nMATH:{self.sub2}\nCHEM:{self.sub3}\nI4:{self.sub4}")
    def percentage(self):
        print('the total percentage obatained is:',((self.sub1+self.sub2+self.sub3+self.sub4)/80)*100)
student1=student(input('enter your name:'),int(input('enter rollno:')))
student1.marks(int(input('enter OOPS marks:')),int(input('enter MATH marks:')),int(input('enter CHEM marks:')),int(input('enter I4 marks:')))
student1.percentage()