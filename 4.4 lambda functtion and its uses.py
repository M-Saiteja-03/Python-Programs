l=[1,2,3,4,5,6,7,8,9,10]
l1=list(filter(lambda x:x%2==0,l))
print(l1)

p=[1,2,3,4,5]
q=[6,7,8,9,10]
x=list(map(lambda x,y:x*y,p,q))
print(x)

import functools
num=[1,2,3,4,5]
mul=functools.reduce(lambda x,y:x*y,num)
print(mul)

