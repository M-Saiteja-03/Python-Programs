class Count:
    Uppercase=0
    Spaces=0
    Vowels=0
    Lowercase=0
    Words=0
    Lines=1
    def __init__(self):
        self.string=input('enter the string:')
    def check(self):
        for i in self.string:
            if i.isupper():
                self.Uppercase+=1
            if i.isspace():
                self.Spaces+=1
            if i.islower():
                self.Lowercase+=1
            if i=='\n':
                self.Lines+=1
    def getCount(self):
        print('Uppercase:',self.Uppercase)
        print('Lowercase:',self.Lowercase)
        print('spaces:',self.Spaces)
        print('Lines:',self.Lines)
        lower_case=self.string.lower()
        for i in lower_case:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                self.Vowels+=1
        print('Vowels:',self.Vowels)
        words=self.string.split(' ')
        print('words:',len(words))
        print('No.of Characters:',len(self.string))
s1=Count()
s1.check()
s1.getCount()




