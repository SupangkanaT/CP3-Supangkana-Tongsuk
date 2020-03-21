
def logIn():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Done!!")
        print("----------Shop----------")
        print("1. Vat Calculator")
        print("2. Price Calculator")
        return True
    else:
        return False

def showMenu():
    print("Done!!")
    print("----------Shop----------")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def selectMenu():
    userSelected = int(input(">>"))
    return userSelected

def vatCalaulate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalaulate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalaulate(price1 + price2)

if logIn():
    showMenu()
    selectMenu()
    print(priceCalaulate())
else:
    print("  >> Username or Password is wrong<< ")
