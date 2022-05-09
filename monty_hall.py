from random import randint


inf, sup = 1, 3
doors = list(range(inf, sup+1))

def userChoice():
    choice=int(input("Choose a door's number :\n"))
    return choice

def testChange(choice1, choice2):
    if(choice1 == choice2):
        return False
    else:
        return True
    
def openDoor(gift, choice, doors):
    if(choice != gift):
        doors.remove(choice)
        doors.remove(gift)
        openedDoor = doors[0]
        
    else:
        doors.remove(choice)
        pos = randint(1, len(doors))
        openedDoor = doors[pos-1]
    
    doors.clear()
    doors.extend(list(range(inf, sup+1)))
    
    return openedDoor
    
def xor(x, y):
    return bool((x and not y) or (not x and y))