a,b,c=[eval(x) for x in input("enter values of a,b,c:").split()]
min=a if a<b and a<c else b if b<c else c
print('the minimum value is:',min)



