class Father:
    def f1(self):
        print('this is father class')
    def family(self):
        print('father:We are one family')

class Mother:
    def m1(self):
        print('this is mother class')
    def family(self):
        print('mother:We are one family')

class Son(Father,Mother):
    def s1(self):
        print('this is son class')
    # def family(self):
    #     print('son:We are one family')

s=Son()
s.f1()
s.m1()
s.s1(),s.family()