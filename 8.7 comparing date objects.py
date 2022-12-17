class Date:
    def init(self):

        d = m = y = 0

    def get(self):

        self.d = int(input("Enter the day: "))
        self.m = int(input("Enter the month: "))
        self.y = int(input("Enter the year: "))


    def __eq__(self, D):
       flag = False
       if self.d == D.d:
           if self.m == D.m:
               if self.y == D.y:
                   flag = True
       return flag


    def __lt__(self, D):
        flag = False


        if self.y <= D.y:
            if self.m <= D.m:
                if self.d <= D.d:
                    flag = True
        return flag
d1 = Date()
d1.get()
d2 = Date()
d2.get()
print("d1==d2", d1 == d2)
print("d1<d2", d1 < d2)
print("d1>d2", d1 > d2)
