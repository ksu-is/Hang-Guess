import time
import random

easy = ['','','','','']

normal = ['','','','','','']

expert = ['','','','','','']

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
