print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))

if height >= 120:
    print("You are allowed to ride the rollercoaster!")
    age = int(input("To know your ride fee, declare your age: \n"))
    if age <= 13:
        print("To take the ride You need to pay 20 naira")
    elif age <= 19:
        print("To take the ride You need  to pay 30 naira")
    elif age <= 30:
        print("Oh ye adult, Your ride fee is 50 naira")
    else:
        print("Ancient one, You need to pay 100 naira")

else:
    print("Get thee behind me, you dwarf")
