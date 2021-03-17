from random import randint

def generateANumber():
    return randint(1, 99)

def stillHaveChance(tryTimes, TotalTimes):
    if tryTimes <= TotalTimes:
        return True
    return False

def tryTimesLeft(tryTimes, TotalTimes):
    return TotalTimes - tryTimes

def isValidInput(guessNum):
    try:
        int(guessNum)
        if int(guessNum) < 1 or int(guessNum) > 99:
            return False
        return True
    except:
        return False

def win(guessNum, myNum):
    if guessNum != myNum:
        return False
    return True

def feedback(guessNum, myNum):
    if guessNum < myNum:
        return "go higher"
    elif guessNum > myNum:
        return "go lower"
    else:
        return "you win"
