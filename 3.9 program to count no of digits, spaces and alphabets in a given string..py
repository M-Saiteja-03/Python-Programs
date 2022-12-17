string='Hello my name is Marepally Saiteja and I belong to the college CBIT CSE3'
print(string)
alphabet,digit,space=0,0,0
for i in string:
    if(i.isalpha()):
        alphabet+=1
    if(i.isspace()):
        space+=1
    if(i.isdigit()):
        digit+=1

print(f'No.of alphabtes={alphabet}')
print(f'No.of spaces={space}')
print(f'No.of digits={digit}')

