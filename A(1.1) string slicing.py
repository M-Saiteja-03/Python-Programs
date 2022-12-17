string1='ABCDCDC'
string2=input("enter the string to find how many times it has occured:")
count=0
for i in range(len(string2),len(string1)+1):
    c=string1[i-len(string2):i]
    if(c==string2):
        count+=1
print(f'{count} times')
