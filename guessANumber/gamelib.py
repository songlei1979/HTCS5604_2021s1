from random import randint

def randomNumber():
    return randint(1, 99)

def inputNumber():
    return input("Please input your number: ")

def isValidInput(num):
    try:
        int(num)
        if isNumInRange(int(num)):
            return False
        return True
    except:
        return False

def isNumInRange(num):
    if num < 100 and num > 0:
        return False
    return True

def isWin(guessNum, myNumber):
    if guessNum == myNumber:
        return True
    return False

def isOutOfTry(iteration, trytime):
    if iteration >= trytime:
        return True
    return False

def hints(guessNum, myNum):
    if guessNum < myNum:
        return "higher"
    elif guessNum > myNum:
        return "lower"
    else:
        return "Wow"