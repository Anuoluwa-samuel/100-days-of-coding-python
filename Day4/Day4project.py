import random 

print("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors.")
user = input(">").lower()

if user == 0:
    print(r'''
          _______
      ---'   ____)
            (_____)
            (_____)
             (____)
      ---.__(___)

          ''')
elif user == 1:
    print(r'''
          _______
      ---'   ____)____
                ______)
                _______)
                _______)
      ---.__________)
          ''')
else:
    print(r'''
          _______
      ---'   ____)____
                ______)
             __________)
             (____)
      ---.__(___)
          ''')
    
computer = random.randint(0, 2)
if computer == 0:
    print(r'''
         _______
      ---'   ____)
            (_____)
            (_____)
             (____)
      ---.__(___)

      ''')
elif computer == 1:
    print(r'''
          _______
      ---'   ____)____
                ______)
                _______)
                _______)
      ---.__________)
          ''')
    
else:
    print(r'''
          _______
      ---'   ____)____
                ______)
             __________)
             (____)
      ---.__(___)
          ''')

if user == computer:
    print("It's a tie!")
elif user == 0:
    computer == 1
    print("Rock smashes scissors! You win!")
elif user == 1:
    computer == 0
    print("Paper covers rock! You win!")
