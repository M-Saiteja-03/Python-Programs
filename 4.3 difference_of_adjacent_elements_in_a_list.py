def diffrence(list):
    flag=1
    for i in range(2,len(list)):
        if abs(list[i-1]-list[i-2])>=abs(list[i]-list[i-1]):
            flag=0
            
    if flag==1:
        return True

    else:
        return False 

    
list=[int(x) for x in input("enter the list of no's:").split()]
x=diffrence(list)

if (x):
    print("True,the absolute difference between each adjacent pair of elements strictly increases.")
else:
    print("False,the absolute difference between each adjacent pair of elements does not increase.")
    
