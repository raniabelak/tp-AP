name=str(input('please enter your name: '))

Tcost= 15.5
if name.lower()=='vip':
    print("enjoy the show for free!")
else:
    tickets= int(input("How many tickets would you like to buy?"))
    cost = tickets*Tcost
    print("the total price is",cost)