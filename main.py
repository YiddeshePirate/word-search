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

directions = {"straight": (0, 1), "down": (1, 0), "diagonal1": (-1, 1), "diagonal2": (1, -1)}

def getlocs(ln, origin, direction):
    x, y = origin
    d, b = direction
    return [(x+i*d, y+i*b) for i in range(ln)]

# print(random.choice(directions.keys()))

# print(getlocs(5, (9, 2), directions["straight"]))

def putword(wrd):
    direction = random.choice(list(directions.values()))
    bkg = random.choice([-1, 1])
    direction = [x*bkg for x in direction]
    print(direction)


    # btm, top, lft, rgt = itertools.chain()
    # print(direction)
    indexes = [(x, y) for x in range(0, 15) for y in range(0, 15)]



putword("dasf")