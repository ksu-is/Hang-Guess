import time
import random

Short = ['Read','Play','Guess','',''] #4-5

Medium = ['','','','','',''] #6-8

Long = ['','','','','',''] #9<

def mask_word(word):
    anon_word = '_' * len(word)
    return anon_word

def known_word(word, anon_word, guess):
    i = 0
    anon = list(anon_word)
    for w in word:
        if guess.lower() == w:
            anon[i] = guess
        i += 1
    return "".join(anon)

def choosenword(word_list):
    word = random.randint(0, len(word_list) - 1)
    return word_list[word]

def choooselist(num):
    if num == "1":
        return Short
    if num == "2":
        return Medium
    if num == "3":
        return Long

def choosedifficulty(num):
    if num == "1":
        return 9
    if num == "2":
        return 6
    if num == "3":
        return 3
        
difficulty = 10
word_guessed = False
game_over = False
guessed_letters = ''
over = ''
again = 'n'
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

while game_over == False:
    if over.lower() == 'q':
        break
    chooseWords = input('''Please choose the length of the word:
    1 = Short Word (4-5 letters)
    2 = Medium Word (6-8 letters)
    3 = Long Word (9 letters and up)\n''')

    answer = choosenWord(chooselist(chooseWords))

    chooseDiff = input('''Please choose how difficult you want the game to be:
    1 = Easy (9 wrong letters)
    2 = Normal (6 wrong letters)
    3 = Hard (3 wrong letters)\n''')

    difficulty = choosedifficulty(chooseDiff)

    maskedWord = mask_word(answer)
    print('Your word will be below. You have',difficulty,'wrong guesses available.\n' + 
    maskedWord)
