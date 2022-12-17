class Grand:
    def __init__(self,grandfname):
        self.grandfname=grandfname
class father(Grand):
    def __init__(self,fathername,grandfname):
        self.fathername=fathername
        super().__init__(grandfname)
class son(father):
    def __init__(self,sonname,fathername,grandfname):
        self.sonname=sonname
        super().__init__(fathername,grandfname)
    def get_detalils(self):
        print('grandfathername:',self.grandfname)
        print('fathername:',self.fathername)
        print('sonname:',self.sonname)
Saiteja=son('saiteja','satyamurthy','Kailasam')
Saiteja.get_detalils()
print(Saiteja.grandfname)
