

def getlimr(di, ln):
    if di == 0:
        return list(range(15))
    elif di == 1:
        return list(range(15-ln))
    else:
        return list(range(ln, 15))


print(getlimr(-1, 4))