# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. 
# bmi is equal to the person's weight divided by the person's height squared.

Weight = float(input("Enter your weight in KG\n"))
Height = float(input("Enter your height in m\n"))

BMI = float(Weight / (Height)**2)

print(f"You currently weigh {Weight} kg and you are {Height} m tall, therefore your BMI is {BMI}")