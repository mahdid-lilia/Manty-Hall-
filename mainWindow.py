import pygame
from pygame.locals import *
from matplotlib.style import use
from monty_hall import *
from random import randint
# Global variables
global mx
global my

# Functions


def testPosition(list=[0, 0], mode='h'):
    if len(list) == 2:
        if mode == 'h':
            return mx >= list[0] and mx <= list[1]
        elif mode == 'v':
            return my >= list[0] and my <= list[1]
    elif len(list) == 4:
        return mx >= list[0] and mx <= list[1] and my >= list[2] and my <= list[3]


def bgFill(x, y, width, height):
    screen.blit(pygame.transform.scale(
        bg.subsurface(x, y, width, height), (width, height)), [x, y])


# Set background music
pygame.mixer.init()
s = 'assets/sounds/'
music = pygame.mixer.music.load(s+'bgSound.mp3')

fail = pygame.mixer.Sound(s+'fail-game.mp3')
win = pygame.mixer.Sound(s+'win-game.mp3')
changeDoor = pygame.mixer.Sound(s+'changeDoor.wav')


pygame.mixer.music.play(-1)
# Initialization
pygame.init()
size = width, height = 1000, 500
screen = pygame.display.set_mode(size)

score = 0
nbr = 0

# Import Images
i = "assets/images/"
closedDoor = pygame.image.load(i+'closedDoor.png').convert_alpha()
openedDoor = pygame.image.load(i+'openedDoor.png').convert_alpha()
giftImg = pygame.image.load(i+'gift.png').convert_alpha()
buttonGame = pygame.image.load(i+'button-play.png').convert_alpha()
buttonAgain = pygame.image.load(i+'button-tryagain.png').convert_alpha()
bg = pygame.image.load(i+'bg.jpg').convert_alpha()
bg = pygame.transform.scale(
    bg, size)

screen.blit(bg, [0, 0])

sizeClosedDoor = (200, 400)
doorSpacing = (height-sizeClosedDoor[1])/2
positionClosedDoor = [[doorSpacing, doorSpacing], [doorSpacing+sizeClosedDoor[0] +
                                                   doorSpacing, doorSpacing], [doorSpacing+2*(sizeClosedDoor[0]+doorSpacing), doorSpacing]]
#*******************#
btnPlaySize = (150,     50)

btnPlayPos = [width-200, 50]
verticalSpacing = 180
btnAgainPos = [btnPlayPos[0], btnPlayPos[1]+verticalSpacing]
textPos = [btnAgainPos[0]+17, btnAgainPos[1]+verticalSpacing]

screen.blit(pygame.transform.scale(
    buttonGame, btnPlaySize), btnPlayPos)
screen.blit(pygame.transform.scale(
    buttonAgain, btnPlaySize), btnAgainPos)
# Show score
textColor = (255, 255, 255)

font = pygame.font.Font('freesansbold.ttf', 20)
# Wrap it inside function
text = font.render('SCORE : 0', True, textColor)
textRect = text.get_rect()
textRect.x, textRect.y = textPos[0], textPos[1]


run = True

verif = True
compt = 2
while run:

    screen.blit(text, textRect)
    # Mouse events
    # Mouse motion
    mx, my = pygame.mouse.get_pos()
    loc = [mx, my]

    # Show images
    if compt == 2:
        screen.blit(pygame.transform.scale(
            closedDoor, sizeClosedDoor), positionClosedDoor[0])
        screen.blit(pygame.transform.scale(
            closedDoor, sizeClosedDoor), positionClosedDoor[1])
        screen.blit(pygame.transform.scale(
            closedDoor, sizeClosedDoor), positionClosedDoor[2])

    # Event manager
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            if left:
                gift = randint(inf, sup)
                if (testPosition(list=[doorSpacing, doorSpacing + sizeClosedDoor[1]], mode='v')):
                    if(testPosition(list=[positionClosedDoor[0][0], positionClosedDoor[0][0]+sizeClosedDoor[0]])):
                        if compt == 2:
                            choice1 = 1
                            compt -= 1
                        elif compt == 1:
                            choice2 = 1
                            compt -= 1

                    elif(testPosition(list=[positionClosedDoor[1][0], positionClosedDoor[1][0]+sizeClosedDoor[0]])):
                        if compt == 2:
                            choice1 = 2
                            compt -= 1
                        elif compt == 1:
                            choice2 = 2
                            compt -= 1
                    elif(testPosition(list=[positionClosedDoor[2][0], positionClosedDoor[2][0]+sizeClosedDoor[0]])):
                        if compt == 2:
                            choice1 = 3
                            compt -= 1
                        elif compt == 1:
                            choice2 = 3
                            compt -= 1
                    # Start game
                    if compt == 1:
                        door = openDoor(gift, choice1, doors)

                        bgFill(positionClosedDoor[door-1][0], positionClosedDoor[door-1]
                               [1], sizeClosedDoor[0], sizeClosedDoor[1])
                        screen.blit(pygame.transform.scale(
                            openedDoor, sizeClosedDoor), positionClosedDoor[door-1])
                    elif compt == 0:
                        compt -= 1
                        change = testChange(choice1, choice2)
                        test = xor(gift == choice1, change)

                        if door == choice2:
                            pygame.mixer.Sound.play(changeDoor)
                            print("The door is already opened")
                            compt = 1
                        elif test:
                            pygame.mixer.Sound.play(win)
                            nbr += 1
                            bgFill(
                                positionClosedDoor[choice2-1][0], positionClosedDoor[choice2-1][1], sizeClosedDoor[0], sizeClosedDoor[1])

                            screen.blit(pygame.transform.scale(
                                giftImg, sizeClosedDoor), positionClosedDoor[choice2-1])
                            score += 1
                            print("You won")
                            bgFill(textRect.x, textRect.y,
                                   textRect.width, textRect.height)
                        else:
                            pygame.mixer.Sound.play(fail)
                            nbr += 1
                            bgFill(
                                positionClosedDoor[choice2-1][0], positionClosedDoor[choice2-1][1], sizeClosedDoor[0], sizeClosedDoor[1])
                            screen.blit(pygame.transform.scale(
                                openedDoor, sizeClosedDoor), positionClosedDoor[choice2-1])
                            print("You lost")
                            bgFill(textRect.x, textRect.y,
                                   textRect.width, textRect.height)

                if (testPosition([btnPlayPos[0], btnPlayPos[0]+btnPlaySize[0], btnPlayPos[1], btnPlayPos[1]+btnPlaySize[1]])):
                    verif = True
                    compt = 2
                if (testPosition([btnAgainPos[0], btnAgainPos[0]+btnPlaySize[0], btnAgainPos[1], btnAgainPos[1]+btnPlaySize[1]])):
                    nbr = 0
                    score = 0
                    verif = True
                    compt = 2
                    bgFill(textRect.x, textRect.y,
                           textRect.width, textRect.height)

                    # pygame.draw.rect(screen, color, pygame.Rect(
                    # textRect.x, textRect.y, textRect.width, textRect.height))

    if verif:
        gift = randint(inf, sup)
        verif = False

    # Show score

    text = font.render('SCORE : '+str(score)+'\\' +
                       str(nbr), True, textColor)
    textRect = text.get_rect()
    textRect.x, textRect.y = textPos[0], textPos[1]

    keys = pygame.key.get_pressed()
    # Update window
    pygame.display.update()


# Close Pygame
pygame.quit()
