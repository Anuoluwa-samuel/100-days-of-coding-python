print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("To know your ride fee, declare your age: \n"))
    if age <= 13:
        print("To take the ride you are to pay 20 naira")
    elif age <= 19:
        print("To take the ride you are to pay 30 naira")
    else:
        print("Oh ye adult, your ride fee is 50 naira")

else:
    print("Get thee behind me, you dwarf")
