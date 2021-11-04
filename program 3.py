def getMoney():
    _money = int(input("How much is your money? "))
    return _money

def getApple():
    _apple = int(input("How much is the price of 1 apple? "))
    return _apple

def getQuantity():
    _quantity = money // apple
    return _quantity

def getTotal():
    _total = quantity * apple
    return _total

def getChange():
    _change = money - total
    return _change

def display(quantityf, changef):
    print(f"You can buy {quantityf} apples and your change is {changef} pesos.")
money = getMoney()

apple = getApple()

quantity = getQuantity()

total = getTotal()

change = getChange()

display(quantity, change)