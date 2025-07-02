print("Welcome to the tip calculator")
bill = float(input("What was the total bill: \n"))
tip = int(input("How much tip would you like to give?, $10, $12 or $20? \n"))
if tip == 10 :
    tip = 0.1

print(f"Tip amount is ${tip * bill}")




