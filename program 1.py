def getName():
    _name = input("Name: ")
    return _name

def getAge():
    _age = input("Age: ")
    return _age

def getAddress():
    _add = input("Address: ")
    return _add

def display(namef, agef, addf):
    print(f"Hi, my name is {namef}. I am {agef} years old and I live in {addf}.")

name = getName()

age = getAge()

address = getAddress()

display(name, age, address)