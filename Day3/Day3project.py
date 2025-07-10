print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road. where do you want to go?")
road = input("Type 'left' to go left or 'right' to go right\n")
if road == "left":
    print("You have come to a lake. There is an island in the middle of the lake")
    Lake = input("Type 'wait' to wait for a boat or 'swim' to swim across\n")
    if Lake == "wait":
        print("You arrived at the island unarmed. There is a house with 3 doors ")
    else:
        print("You drowned in the lake. GAME OVER")
    Door = (input("One is red, One is yellow, One is blue, which one would you open\n"))
    if Door == "red":
        print("You got burned by fire. GAME OVER")
    elif Door == "yellow" :
        print("You just met your nemesis. GAME OVER ")
    else:
        print("You got the treasure, Congratulations. YOU WIN")

else:
    print("You fell into a hole. GAME OVER")