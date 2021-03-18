from library import generateANumber, stillHaveChance, win, isValidInput, tryTimesLeft, feedback

myNum = generateANumber()

tryTime = 0
TotalTime = 10
guessNum = 0
while stillHaveChance(tryTime, TotalTime) and (not win(guessNum, myNum)):
    print("you have " + str(tryTimesLeft(tryTime, TotalTime)) + " chances left")
    guessNum = input("please guess number")
    if isValidInput(guessNum):
        guessNum = int(guessNum)
        print(feedback(guessNum, myNum))
    else:
        print("you should input a number between 0 to 100")
    tryTime = tryTime + 1

if not stillHaveChance(tryTime, TotalTime):
    print("YOU LOOOOOOOOOOSE!")