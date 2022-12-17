class bank:
    def deposit(self):
        money=float(input("enter the amount to be deposited:"))
        self.balance+=money
        print('your amt has been successfully deposited.....')
        print(f'your account balance is Rs.{self.balance}')
        pass
    def withdraw(self):
        money = float(input("enter the amount to be withdrawn:"))
        self.balance -= money
        print('your amt has been successfully withdrawn.....')
        print(f'your account balance is Rs.{self.balance}')
    def show_balance(self):
        print(f'your account balance is Rs.{self.balance}')
customer1=bank()
customer1.balance=10000
customer1.name = input('enter your name:')
print(f'Welcome to HDFC Bank,{customer1.name}')
print('choose any1 of the option below:')
print('1.deposit','2.withdraw','3.show balance amount',sep='\n' )
option=int(input('enter your choice:'))
if option==1:
    customer1.deposit()
if option==2:
    customer1.withdraw()
if option==3:
    customer1.show_balance()

