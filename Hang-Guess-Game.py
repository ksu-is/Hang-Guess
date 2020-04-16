import time
import random

Short = ['','','','','']

Medium = ['','','','','','']

Long = ['','','','','','']

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

def List(num):
    if num == "1":
        return Short
    if num == "2":
        return Medium
    if num == "3":
        return Long

def difficulty(num):
    if num == "1":
        return 10
    if num == "2":
        return 7
    if num == "3":
        return 4
