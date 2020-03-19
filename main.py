import numpy as np
import random

board = np.empty([15, 15], dtype="U1")
board[:] = " "
# print(board)


# print(itertools.permutations(range(15), range(15), ))

indexes = [(x, y) for x in range(15) for y in range(15)]

# print(random.choice(indexes))

directions = {"straight": (0, 1), "down": (1, 0), "diagonal1": (1, 1), "diagonal2": (-1, 1)}

def getlocs(ln, origin, direction):
    """ Gets the indexes given a direction, starting point, length"""
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
    elif:
        return list(range(ln, 15))

def place_word(word):
    not_put = True
    while not_put:
        direction = random.choice(list(directions.values()))
        bkg = random.choice([-1, 1])
        direction = [x*bkg for x in direction]
        starts = random.choice(posstarts(word, direction))
        locs = getlocs(len(word), starts, direction)
        print(locs)
        if is_good_locs(word, locs):
            print(direction)
            print(starts)
            for x, y in zip(locs, word):
                board[x] = y
            not_put = False


def is_good_locs(word, locs):
    def cl(char, loc):
        if board[loc] == " " or board[loc] == char:
            return True
    return all([cl(x, y) for x, y in zip(word, locs)])
    

def fill_board():
    ltrs = [i for i in np.nditer(board) if i != " "]
    indexes = [(x, y) for x in range(15) for y in range(15)]
    for i in indexes:
        if board[i] == " ":
            board[i] = random.choice(ltrs)
        else:
            pass


print(board)
place_word("hello")
place_word("goodbye")
place_word("hola")
place_word("howdy")

print(board)




fill_board()

print(board)