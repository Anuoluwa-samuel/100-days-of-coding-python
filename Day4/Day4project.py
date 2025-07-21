if User == "rock" and Computer == "scissors":
    print("User wins")

if User == "scissors" and Computer == "paper":
    print("User wins")

if User == "paper" and Computer == "rock":
    print("User wins")

if User == Computer:
    print("It's User tie")

if (User == "scissors" and Computer == "rock") or \
   (User == "paper" and Computer == "scissors") or \
   (User == "rock" and Computer == "paper"):
    print("Computer wins")