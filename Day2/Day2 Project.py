print("Welcome to the tip calculator")
bill = input("What was the total bill: \n")
tip = input("How much tip would you like to give?, $10, $12 or $20? \n")
if tip == 10 :
    tip = 0.1,
elif tip == 12:
    tip = 0.12,
elif tip == 15:
    tip = 0.15,
else:
    tip = float(tip/100, 2)
print(tip)