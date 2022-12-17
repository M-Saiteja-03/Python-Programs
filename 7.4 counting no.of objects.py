class Student:
    count=0
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        Student.count+=1
        print('hello',self.name,'!!')
        print('your rollno:',self.roll,'!!')
s1=Student('Sai Teja',167)
s2=Student('xyz',100)
s3=Student('abc',101)
print('No.of Students are:',Student.count)