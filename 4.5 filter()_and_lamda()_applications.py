S1= ['hi', 'this' , 'is', 'a', 'very', 'simple', 'string' , 'for', 'us']
#in above string find the strings which as length 2 only using filter function with and without lambda function.

'''using lambda()'''
print('using lambda()')
S2=list(filter(lambda x:len(x)==2,S1))
print(S2)

'''without using lambda()'''
print('without using lambda()')
def length_2(s):
    if len(s)==2:
        return True
    
S2=list(filter(length_2,S1))
print(S2)


