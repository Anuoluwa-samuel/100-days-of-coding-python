# BMI Calculator with Interpretations
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
#If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"

Weight = float(input("Enter your weight in KG\n"))
Height = float(input("Enter your height in m\n"))

bmi = Weight / (Height ** 2)

if bmi <= 18.5:
    print("underweight")
elif bmi <= 25:
    print("normal weight")
else:
    print("overweight")
