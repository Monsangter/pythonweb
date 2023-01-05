import random


def getRandomNumber():
    ls = []

    while True:
        number = random.randint(1,45)

        if len(ls) == 6:
            break

        if number not in ls:
            ls.append(number)
    
    ls.sort()

    return ls

for i in getRandomNumber():
    print(i, end = " ")