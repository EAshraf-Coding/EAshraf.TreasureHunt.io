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

choice1 = input("Would you like to go North or South?")
if choice1 in ["North", "north"]:
    choice2 = input("You have come across a vast body of water with an island in the middle. Do you wait for a boat or swim?")
    if choice2 in ["wait" , "Wait"]:
        choice3 = input("Waiting for the boat was the right decision, it takes you to the island. You are then met with three doors. Red, Blue and Yellow. Which door do you enter?")
        if choice3 in ["Blue" , "blue"]:
                print("You entered the correct door. You open the door to see gold further than the eye can see. Vast wealth is yours! You WIN!")
        elif choice3 in ["Red" , "red"]:
                print("You are met with a dragon. It sets you on fire. Start Over.")
        elif choice3 in ["Yellow" , "yellow"]:
                print("A centaur tramples you to death. Start Over.")
    elif choice2 in ["Swim" , "swim"]:
            print("Upon entering the water you realise it is freezing. You freeze to death. Start Over.")
if choice1 in ["south" , "South"]:
    print("You have fallen off the edge of the world. You died. Start Over")
if choice1 in ["East", "east"]:
    print("You have come across an ogre. Would you like to talk to him?")
    choice4 = input("Do you talk to the ogre? Yes or No")
    if choice4 in ["Yes" , "yes" , "y" , "Y"]:
        print("The ogre doesn't want to talk to you. He crushes you with his body. Start Over")
    if choice4 in ["No" , "no" , "N" , "n"]:
        print("The ogre takes this as disrespect and decides to crush you with his body. You died. Start Over.")
if choice1 in ["West" , "west"]:
    print("You have come across a woman in a forest. She is crying. Do you approach her?")
    choice5 = input("Do you approach the crying woman? Yes or No")
    if choice5 in ["Yes" , "yes" , "y" , "Y"]:
        print("The woman looks up at you startled and says \'What do you want?'")
    if choice5 in ["No" , "n" , "no" , "N"]:
        print("You move past the woman and see a waterfall.")