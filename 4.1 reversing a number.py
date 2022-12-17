def reverse_number(n):
    y=0
    while(n):
        rem=n%10
        y=y*10+rem
        n=n//10
    return y

n=int(input("enter a number:"))
y=reverse_number(n)
print('reversed number=',y)
