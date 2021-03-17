import guessANumber.gamelib as g

myNum = g.randomNumber()
timeToTry = 10

i = 0
guessNum = g.inputNumber()
while not g.isValidInput(guessNum):
    print("input a valid number please")
    guessNum = g.inputNumber()
guessNum = int(guessNum)


while (not g.isOutOfTry(i, timeToTry)) and (not g.isWin(guessNum,myNum)):
    print(g.hints(guessNum, myNum))
    guessNum = g.inputNumber()
    while not g.isValidInput(guessNum):
        print("input a valid number please")
        guessNum = g.inputNumber()
    guessNum = int(guessNum)
    i = i + 1

if (not g.isOutOfTry(i, timeToTry)) and (g.isWin(guessNum,myNum)):
    print("you win")
else:
    print("you lose")