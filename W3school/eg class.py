# class bankacount :
#     def __init__(self,acount_holder,balance):
#         self.acount_holder = acount_holder
#         self.balance = balance

#     def deposite(self,amount):
#         self.balance += amount
#         print(f'{amount} is deposite successfully')
#         print(f'Your Total balance is {self.balance}')
    
#     def withdrow(self,amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f'{amount} is withdrow successfully')
#         else :
#             print('Insufficient acoount balance')
#         print('Your Total balance is',self.balance)

# AC1 = bankacount('Syman',50000)

# AC1.deposite(10000)
# AC1.withdrow(5000)


class shopping_cart:
    def __init__(self):
        self.items = []
    
    def item_add(self,item_name):
        self.items.append(item_name)
        print(f'{item_name} is added successfully')
    
    def remove(self,item_name):
        if item_name in self.items:
            self.items.remove(item_name)
            print(f'{item_name} removed successfully')
        else :
            print(f'{item_name} not found in cart')

    def show_cart(self):
        if self.items :
            print('items in your cart')
            for i in self.items:
                print(i)
        else:
            print('Your cart is empty')
    



cart1 = shopping_cart()

cart1.item_add('Orange')
cart1.item_add('Banana')
cart1.item_add('Apple')
cart1.show_cart()
cart1.remove('Banana')
cart1.remove('Mango')
cart1.show_cart()
        


        