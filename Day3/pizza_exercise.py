print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    price = 15 
    if pepperoni == "Y":
        price += 2
    if pepperoni == "N":
        price == 15
        if extra_cheese == "Y":
            price += 1
        else:
            price == 15
            print(f"Your final bill is {price}")
elif size == "M":
    price = 20
    if pepperoni == "Y":
        price += 3
    elif pepperoni == "N":
        price == 20
        if extra_cheese == "Y":
            price += 1
        else:
            price == 20
        
elif size == "L":
    price = 25
    if pepperoni == "Y":
        price += 3
    else:
        price == 25
        if extra_cheese == "Y":
            price += 1
        else:
            price == 20

print(f"Your final bill is {price}")
