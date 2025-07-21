import random 

print("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors.")
game = input(">").lower()

if game == 0:
    print(r'''
          _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)

          ''')
elif game == 1:
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
    
    
print(random.choice(computer))
