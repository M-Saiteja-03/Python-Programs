class Test:
    wheels=4
    @classmethod
    def Cmtd(cls,name):#cls keyword
        print('You are using class method')
        print(f'{name} has {cls.wheels} wheels')
    @staticmethod
    def Smtd():#No arguments like self,cls etc are required in static method
        print('\n')
        print('You are using static method')
Test.Cmtd('car')
Test.Smtd()
