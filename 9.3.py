from re import *
pattern=compile("TS")
x=input("enter the car number:")
matched=match(pattern,x)
if matched:
    print("car is registered in telangana")
else:
    print("car is not registered in telangana")