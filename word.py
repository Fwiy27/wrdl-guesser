import random

with open('words.txt') as file:
    words = file.readlines()
    for i in range(len(words)):
        words[i] = words[i].strip()

def get_words(greens, yellows, reds, list = words):
    checked = list[:]
    # Greens
    for green in greens:
        for i in range(len(checked) - 1, -1, -1):
            if green[0] != checked[i][green[1]]:
                checked.pop(i)
    # Yellows
    for yellow in yellows:
        for i in range(len(checked) - 1, -1, -1):
            if yellow[0] not in checked[i]:
                checked.pop(i)
            elif yellow[0] in checked[i] and yellow[0] == checked[i][yellow[1]]:
                checked.pop(i)

    # Reds
    for red in reds:
        for i in range(len(checked) - 1, -1, -1):
            if in_list(red[0], greens) or in_list(red[0], yellows):
                if red[0] == checked[i][red[1]]:
                    checked.pop(i)
            elif red[0] in checked[i]:
                checked.pop(i)
    return random.choice(checked)


def in_list(letter, list):
    for l in list:
        if l[0] == letter:
            return True
    return False