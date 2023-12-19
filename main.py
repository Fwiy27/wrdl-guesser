from word import *
from os import system

def remove_dupes(list) -> list:
    ret = []
    for i in range(len(list) - 1, -1, -1):
        temp = list[i]
        list[i] = None
        if temp not in list:
            ret.append(temp)
    return ret

def extract(guess) -> list:
    greens = []
    yellows = []
    reds = []
    colors = input('Colors: ').lower()
    for i in range(len(colors)):
        match colors[i]:
            case 'g':
                greens.append([guess[i], i])
            case 'y':
                yellows.append([guess[i], i])
            case 'r':
                reds.append([guess[i], i])
    return [greens, yellows, reds]

greens = []
yellows = []
reds = []
guess = input('Guess: ')
colors = extract(guess)
while True:
    system('clear')
    if colors[0]:
      greens+=colors[0]
      greens = remove_dupes(greens)
    if colors[1]:
      yellows+=colors[1]
      yellows = remove_dupes(yellows)
    if colors[2]:
      reds+=colors[2]
      reds = remove_dupes(reds)
    word = get_words(greens, yellows, reds)
    input(word)
    colors = extract(word)
