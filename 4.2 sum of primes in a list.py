def sum_of_primes(l):
    s=0
    for x in l:
        if(x==1):
            continue
        flag=1
        if x>0:
            for i in range(2,x):
                if(x%i==0):
                    flag=0
            if(flag==1):
                 s=s+x
    return(s)
l=[int(x) for x in input("enter the list of no's:").split()]
print(l)
s=sum_of_primes(l)
print(s)



