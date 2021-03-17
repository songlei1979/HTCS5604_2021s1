from random import randint

def generateANumber():
    return randint(1, 99)

def isOutOfTry(tryTimes, TotalTimes):
    if tryTimes <= TotalTimes:
        return False
    return True
