if user == "rock" and b == "scissors":
    print("user wins")

if user == "scissors" and b == "paper":
    print("user wins")

if user == "paper" and b == "rock":
    print("user wins")

if user == b:
    print("It's user tie")

if (user == "scissors" and b == "rock") or \
   (user == "paper" and b == "scissors") or \
   (user == "rock" and b == "paper"):
    print("b wins")