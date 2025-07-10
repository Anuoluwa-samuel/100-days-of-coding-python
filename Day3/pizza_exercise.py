print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


if size == "S", :
    price = 15 
    
elif size == "M":
    price = 20
elif size == "L":
    price = 25
else:
    print("Invalid size. Please choose S, M or L.")