#I want to sell a house whose measurements are given in sqft, but the sale is accepted in sqmt.
#If the price of the house of 100sqft is Rs 5000, then how much amount of money will I get if I get to
#sell 5 such houses. Write a python code which accepts input in sqft but gives the total price as the output.

def sell(y,n):
    print('the total price for selling 5 such houses in sqmt are:')
    print(y*5)
    print('the amount in sqft is:')
    print(n*50)

n=int(input('enter how many sqft your house is:'))
a=n/10.764
print('the area you entered in sqft is:',a)
x=n*50
y=x/10.764
sell(y,n)