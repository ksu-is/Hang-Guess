import time
import random

score = 0

def difficultyEASY():
    diff = input("Do you want to change the difficulty?. Or quit the game? ")
    if diff in ["yes", "y"]:
        difficulty()
    elif diff in ["no", "n"]:
        easy()   
    else:
        quit()

#whether they want to try a diffirent difficulty or stay on medium
def difficultyMED():
    diff = input("Do you want to change the difficulty?. Or quit the game? ")
    if diff in ["yes", "y"]:
        difficulty()
    elif diff in ["no", "n"]:
        med()   
    else:
        quit()


#whether they want to try a diffirent difficulty or stay on hard
def difficultyHARD():
    diff = input("Do you want to change the difficulty?. Or quit the game? ")
    if diff in ["yes", "y"]:
        difficulty()
    elif diff in ["no", "n"]:
        hard()
    else:
        quit()





