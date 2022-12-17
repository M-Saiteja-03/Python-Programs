#. WAP that has a class Store which keeps a record of code and price of each product. Display a menu of all products
# to the user and prompt him to enter the quantity of each item required. Generate a bill and display the total amount.
'''try this question by the concept of 6.4 when u are free!!!'''
class store:
    prod_code=[]
    prod_name=[]
    prod_price=[]
    prod_quantity=[]
    def Product_Detalis(self):
        for i in range(n):
            self.prod_name.append(input('enter product name:'))
            self.prod_code.append(int(input("enter product code:")))
            self.prod_price.append(int(input("enter the price of the product:")))
    def get_details(self):
        print('-----------------------------------------------------------')
        print("Product Name\t\tProduct Code\t\tProduct Prize")
        print('-----------------------------------------------------------')
        for i in range(n):
            print(self.prod_name[i],'\t\t\t\t\t',self.prod_code[i],'\t\t\t\t\t',self.prod_price[i])
        print('-----------------------------------------------------------')
    def bill(self):
        self.total=0
        for i in range(n):
            self.prod_quantity.append(int(input(f"enter the quantity of product code {self.prod_code[i]}:")))
            self.total=self.total+self.prod_price[i]*self.prod_quantity[i]
        print("Invoice Receipt")
        print("-----------------------------------------------------------------------------")
        print("Product   \tProduct Code   \tQuantity   \tCost Price   \tTotal Amount")
        print("-----------------------------------------------------------------------------")
        for i in range(n):
            print(self.prod_name[i],"\t\t\t\t",self.prod_code[i],"\t\t\t\t",self.prod_quantity[i],"\t\t\t\t",self.prod_price[i], "\t\t\t\t",self.prod_quantity[i] * self.prod_price[i])
            print("-----------------------------------------------------------------------------")
        print("                                              Total Amount = ", self.total)
        print("-----------------------------------------------------------------------------")

products=store()
n=int(input("enter the no.of products:"))
products.Product_Detalis()
products.get_details()
products.bill()
p=[]
p.append(products)
print(p)
