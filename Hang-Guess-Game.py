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

#if the user picked easy for their difficulty
def easy():
    global score 
    print ("\nStart guessing...")

    EASYWORDS = open("Easy.txt","r+")
    words = []
    for item in EASYWORDS:
        words.append(item.strip('\n'))

    time.sleep(0.5)

    word = random.choice(words).lower()
    guesses = ''
    fails = 0
    while fails >= 0 and fails < 10:         
        failed = 0                
        for char in word:      
            if char in guesses:    
                print (char,)

            else:
                print ("_"),     
                failed += 1    
        if failed == 0:        
            print ("\nYou won, GOOD JOB!")
            score = score + 1
            print ("You now have a score of, ", score)
            print('\n')
            difficultyEASY()

        guess = input("\nGuess a letter:").lower()
        while len(guess)==0:
            guess = input("\nTry again:").lower()
        guess = guess[0]
        guesses += guess 
        if guess not in word:
            fails += 1
            print ("\nWrong")

            if fails == 1:
                print ("You have", + fails, "fail....WATCH OUT!" )
            elif fails >= 2 and fails < 10:
                print ("You have", + fails, "fails....WATCH OUT!" )
            if fails == 10:
                print ("You Lose\n")
                print ("You now have a score of, ", score)
                print ("the word was,", word)
                print('\n')
                score = 0
                difficultyEASY()
                
#if the user picked medium for their difficulty
def med():
    global score 
    print ("\nStart guessing...")

    MEDWORDS = open("Med.txt","r+")
    words = []
    for item in MEDWORDS:
        words.append(item.strip('\n'))

    time.sleep(0.5)

    word = random.choice(words).lower()
    guesses = ''
    fails = 0
    while fails >= 0 and fails < 10:           
        failed = 0                
        for char in word:      
            if char in guesses:    
                print (char,)    

            else:
                print ("_"),     
                failed += 1    
        if failed == 0:        
            print ("\nYou won, GOOD JOB!")
            score = score + 1
            print ("You now have a score of, ", score)
            print('\n')
            difficultyMED()

        guess = input("\nGuess a letter:").lower()
        while len(guess)==0:
            guess = input("\nTry again:").lower()
        guess = guess[0]
        guesses += guess   
        if guess not in word:  
            fails += 1        
            print ("\nWrong")

            if fails == 1:
                print ("You have", + fails, "fail....WATCH OUT!" )
            elif fails >= 2 and fails < 10:
                print ("You have", + fails, "fails....WATCH OUT!" ) 
            if fails == 10:           
                print ("You Lose\n")
                print ("You now have a score of, ", score)
                print ("the word was,", word)
                print('\n')
                score = 0 
                difficultyMED()     

#if the user picked hard for their difficulty
def hard():
    global score  
    print ("\nStart guessing...")

    HARDWORDS = open("Hard.txt","r+")
    words = []
    for item in HARDWORDS:
        words.append(item.strip('\n'))

    time.sleep(0.5)

    word = random.choice(words).lower()
    guesses = ''
    fails = 0
    while fails >= 0 and fails < 10:  #try to fix this         
        failed = 0                
        for char in word:      
            if char in guesses:    
                print (char,)    

            else:
                print ("_"),     
                failed += 1    
        if failed == 0:        
            print ("\nYou won, GOOD JOB!")
            score = score + 1
            print ("You now have a score of, ", score)
            print('\n')
            difficultyHARD()

        guess = input("\nGuess a letter:").lower()
        while len(guess)==0:
            guess = input("\nTry again:").lower()
        guess = guess[0]
        guesses += guess   
        if guess not in word:  
            fails += 1        
            print ("\nWrong")

            if fails == 1:
                print ("You have", + fails, "fail....WATCH OUT!" )
            elif fails >= 2 and fails < 10:
                print ("You have", + fails, "fails....WATCH OUT!" ) 
            if fails == 10:           
                print ("You Lose\n")
                print ("You now have a score of, ", score)
                print ("the word was,", word)
                print('\n')
                score = 0 
                difficultyHARD()



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
