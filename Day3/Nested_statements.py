print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you? \n"))
    if age <= 13:
        print("To take the ride you are to pay 20 naira")
    elif age <= 19:
        print("To take the ride you are to pay 30 naira")
    else:
        print("O ye adult, your ride fee is 50 naira")

else:
    print("Sorry your height forbids you from entering" )
