class Employee:
    def __init__(self,name,salary):
        self.n=name
        self.s=salary
    def __mul__(self,x):
        return self.s*x.d
class employeeAttendance:
    def __init__(self,days):
        self.d=days
e=Employee("Saiteja",10000)
days=employeeAttendance(28)
print("Salary per month=",e*days)
