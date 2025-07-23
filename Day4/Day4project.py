import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user=int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
if user == 0:
    print("You chose Rock:")
    print(rock)
elif user == 1:
    print("You chose Paper:")
    print(paper)
elif user == 2:
    print("You chose Scissors:")
    print(scissors)
else:
    print("Invalid input! You lose.")
    exit()

print(user)

computer_choice = random.randint(0,2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if user == computer_choice:
    print("It's a draw!")
elif user == 0 and computer_choice == 2:
    print("You win!")
elif user == 1 and computer_choice == 0:
    print("You win!")
elif user == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You lose!")