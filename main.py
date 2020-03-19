import numpy as np
import random
import string
import itertools

board = np.empty([15, 15], dtype="U1")

# print(board)

lstl = list(string.ascii_lowercase)

# print(itertools.permutations(range(15), range(15), ))

indexes = [(x, y) for x in range(15) for y in range(15)]

# print(random.choice(indexes))

directions = {"straight": (0, 1), "down": (1, 0), "diagonal1": (1, 1), "diagonal2": (-1, 1)}

def getlocs(ln, origin, direction):
    x, y = origin
    d, b = direction
    return [(x+i*d, y+i*b) for i in range(ln)]


def posstarts(wrd, direction):
    ln = len(wrd)-1
    rd, cd = direction
    rl = getlimr(rd, ln)
    cl = getlimr(cd, ln)
    return [(x, y) for x in rl for y in cl]

def getlimr(di, ln):
    if di == 0:
        return list(range(15))
    elif di == 1:
        return list(range(15-ln))
    else:
        return list(range(ln, 15))

def place_word(word):
    direction = random.choice(list(directions.values()))
    bkg = random.choice([-1, 1])
    direction = [x*bkg for x in direction]
    starts = random.choice(posstarts(word, direction))
    locs = getlocs(len(word), starts, direction)
    print(locs)
    print(direction)
    print(starts)
    for x, y in zip(locs, word):
        board[x] = y


# print(board)

place_word("hello")

place_word(("goodbye"))
print(board)



