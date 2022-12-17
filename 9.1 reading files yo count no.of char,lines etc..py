file=open('firstfile.txt','r+')
file.write('Hello This is MY first file In Python in Pycharm IDE')
# data=file.read() we can't read nd write data at a time
# print(data)
file.close()
file=open('firstfile.txt','r')
data=file.read()
print(data)
Uppercase=Spaces=Lowercase=Lines=Words=0
Lines=1
for i in data:
    # print(i)
    # print('-')
    if i.isupper():
        Uppercase += 1
    if i.isspace():
        Spaces += 1
    if i.islower():
        Lowercase += 1
    if i == '\n':
        Lines += 1
words=data.split()
print('words:',len(words))
print('Uppercase:',Uppercase)
print('Lowercase:',Lowercase)
print('spaces:',Spaces)
print('Lines:',Lines)
print('No.of Characters:',len(data))
file.close()