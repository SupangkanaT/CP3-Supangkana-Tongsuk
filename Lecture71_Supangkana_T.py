menuList = []
priceList = []

def showBill():
    print("----Food----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice += int(priceList[number])
    print("Total Price = ", totalPrice)

while True:
    menuName = input("Please Enter menu: ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price: ")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
