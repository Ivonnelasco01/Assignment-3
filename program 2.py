
def getApple():
     _apple = int(input("How many apples will you buy? "))
     return _apple

def getOrange():
    _orange = int(input("How many orange will you buy? "))
    return _orange

def getapplePrc():
    _applePrc= apple * 20
    return _applePrc

def getorangePrc():
    _orangePrc = orange * 25
    return _orangePrc

def gettotal():
    _total = applePrc + orangePrc
    return _total

def display(totalf):
    print(f"The total amount is {totalf} pesos.")

apple = getApple()

orange = getOrange()

applePrc = getapplePrc()

orangePrc = getorangePrc()

total = gettotal()

display(total)
