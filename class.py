import numpy as np
import itertools
import random
import string

directions = [(x*j,y*j) for x,y in [(0, 1), (1, 0), (1, 1), (-1, 1)] for j in [-1, 1]]


class board():

    def __init__(self, size):
        self.board = np.empty([size, size], dtype="U1")
        self.board[:] = " "
        self.words = []
        self.size = size
    
    def add_word(self, word_o):
        
        put = False
        """
        This code must run multiple times until it finds a place for the word
        """
        while not put:
            # pick a random direction
            word_o.direction = random.choice(directions)
            # get a list from the word object of possible places
            starts = word_o.posstarts(self.size)
            # pick a random starting point
            start = random.choice(starts)
            # get all the indexes that it will use
            takes = word_o.getlocs(start)

            # make sure the locations don't have a different characters
            if board.is_good_locs(self, word_o, takes):
                for x, y in zip(word_o.word, takes):
                    self.board[y] = x
                    self.words.append(word_o.word)

                # to break out of the loop
                put = True
            else:
                print("retrying")


    def is_good_locs(self, word_o, locs):
        #mini function for each character

        def cl(char, loc):
            if self.board[loc] == " " or self.board[loc] == char:
                return True

        #make sure it holds true for all instances
        return all([cl(x, y) for x, y in zip(word_o.word, locs)])



    def fill(self):
        ltrs = [i for i in np.nditer(self.board) if i != " "]
        indexes = [(x, y) for x in range(self.size) for y in range(self.size)]
        for i in indexes:
            if self.board[i] == " ":
                self.board[i] = random.choice(ltrs)
            else:
                pass
    

    def __str__(self):
        return self.board.__str__()








class word_obj():
    def __init__(self, word):
        self.word = word
        self.direction = random.choice(directions)
        self.length = len(self.word)


    def posstarts(self, board_size):
        ln = self.length - 1
        rd, cd = self.direction
        rl = word_obj.getlimr(rd, ln, board_size)
        cl = word_obj.getlimr(cd, ln, board_size)
        return [(x, y) for x in rl for y in cl]



    @staticmethod
    def getlimr(di, ln, size):
        if di == 0:
            return list(range(size))
        elif di == 1:
            return list(range(size-ln))
        elif di == -1:
            return list(range(ln, size))


    def getlocs(self, origin):
        """ Gets the indexes given a direction, starting point, length"""
        x, y = origin
        d, b = self.direction
        return [(x+i*d, y+i*b) for i in range(self.length)]





    def __str__(self):
        return self.word
        

def getwordlist(mesg):
    wordlist = input(mesg).strip().split(",")
    letlist = [list(x) for x in wordlist]
    flatletlist = list(itertools.chain(*letlist))
    if all([x in itertools.chain(string.ascii_uppercase, string.ascii_lowercase) for x in flatletlist]):
        return wordlist
    else:
        getwordlist("Try again:\n")
        wordlist = input("").strip().split(",")




def getbsize(mesg):
    bsize = input(mesg)
    try:
        int(bsize)
        return int(bsize)
    except:
        getbsize("Try again:\n")
    


if __name__ == "__main__":
    bsize = getbsize("Enter Board size:\n")
    wordlist = getwordlist("Enter comma separated words: \n")



    brd = board(bsize)
    for i in wordlist:
        j = word_obj(i)
        brd.add_word(j)
    # print(brd)
    brd.fill()
    print(brd)
    with open("page.html", "w") as f:
        for i in range(brd.size):
            x = " ".join(brd.board[i,])
            f.write(f"<h1 style=font-family: Consolas; letter-spacing:101px>{x}</h1>")
