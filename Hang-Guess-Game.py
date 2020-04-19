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

#Where the user picks a difficulty
def difficulty():

    print("easy\n")
    print("medium\n")
    print("hard\n")

    menu=input("Type in what difficulty you would like (type 'h' for hard, 'm' for medium, 'e' for easy, or 'q' to quit)? ").lower()

    if menu in ["hard", "h"]:
        time.sleep(1)
        hard()

    elif menu in ["medium", "m"]:
        time.sleep(1)
        med()

    elif menu in ["easy", "e"]:
        time.sleep(1)
        easy()

    elif menu in ["quit", "q"]:
        quit()

    else:   
        print("Please type in either 'h' for hard, 'm' for medium, or 'e' for easy.")
        time.sleep(1)
        difficulty()   






start = input('''
 __    __       ___       __   __    _______   _______   __    __   _________   _________   _________
|  |  |  |     /   \     |  \ |  |  /  _____| /  _____| |  |  |  | |   ______| |   ______| |   ______|
|  |__|  |    /  ^  \    |   \|  | |  |  __  |  |  __   |  |  |  | |  |______  |  |______  |  |______    
|   __   |   /  /_\  \   |  . `  | |  | |_ | |  | |_ |  |  |  |  | |   ______| |______   | |______   |    
|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |__| |  |  |__|  | |  |______   ______|  |  ______|  |
|__|  |__| /__/     \__\ |__| \__|  \______|  \______|  |________| |_________| |_________| |_________|

#################################
#     Welcome to HangGuess!     #
#         Want to Play?         #
#   Press any button to play!   #
#      Or Press q to quit       #
#################################
''')

if start.lower() == 'q':
    quit()
else:
    name = input('What is your name?')
    print ("\n")
    print('Hello, ' + name, "Time to play HangGuess! You have 10 guesses to win!")
    print ("\n")
    time.sleep(1)
    difficulty()

start()     
