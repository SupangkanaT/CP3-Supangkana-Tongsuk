def vatCalculate(totalprice):
    result = totalprice+(totalprice*7/100)
    return result

inputNumber = int(input("Input Number : "))
print(vatCalculate(inputNumber))
