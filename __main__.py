# importation of libraries
from matplotlib.style import use
from monty_hall import *
from random import randint
# Score's initialization
score = 0
while(True):
    gift = randint(inf, sup)

    choice1 = userChoice()
    door = openDoor(gift, choice1, doors)

    choice2 = userChoice()
    change = testChange(choice1, choice2)

    test = xor(gift == choice1, change)

    if door == choice2:
        print("The door is already opened")
    elif test:
        print("You won")
        score += 1
    else:
        print("You lost")

    print("Your score is: ", score)
