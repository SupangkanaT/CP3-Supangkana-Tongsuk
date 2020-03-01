userName = input("Username: ")
password = input("Password: ")

if userName == "dream" and password == "1234":
    print("-----Hello welcome to dShop-----")
    print("1. Apple 20 (THB)")
    print("2. Watermelons 30 (THB)")
    print("3. juice 50 (THB)")

    userSelected = int(input("\nMenu >> "))
    if userSelected == 1:
        apple = int(input("How many do you want? "))
        result = 20 * apple
        print("Total is ", result, "(THB)")
    elif userSelected == 2:
        watermelons = int(input("How many do you want? "))
        result = 30 * watermelons
        print("Total is ", result, "(THB)")
    else:
        juice = int(input("How many do you want? "))
        result = 50 * juice
        print("Total is ", result, "(THB)")
else:
    print("  >>Username or Password is wrong<<")
