print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill: \n"))
tip = int(input("How much tip would you like to give?, $10, $12 or $15? \n"))
if tip == 10:
    tip = 0.1
elif tip == 12:
    tip = 0.12
elif tip == 15:
    tip = 0.15
else:
    tip = tip/100

people = int(input("How many people are splitting the bill? \n="))
bill = (total_bill + (tip * total_bill)) / (people)
print(f"Each person is to pay ${bill}")




