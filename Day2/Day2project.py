print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill: \n"))
tip = int(input("How much tip would you like to give?, $10, $12 or $15? \n")) / 100
people = int(input("How many people are splitting the bill? \n="))
bill = (total_bill + (tip * total_bill)) / (people)
print(f"Each person is to pay ${bill:.2f}")

# There are more simpler ways to get to the solution    