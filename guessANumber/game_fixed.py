# from random import randint
# # ask computer generate a number
# myNum = randint(1,99)
# start a loop for 10 times
i = 0
while i <= 9: # set 10 times for guessing
    # ask player to input a number
    print("you only " + str(10 - i) + " chances")
    guessNum = input("Please guess a number")
    # verify the input number
    try:
        int(guessNum)
        if int(guessNum) < 1 or int(guessNum) > 99:
            print("please input a number between 1 to 99")
        else: # number is valid
            if int(guessNum) > myNum:
                print("your number is higher")
            elif int(guessNum) < myNum:
                print("your number is lower")
            else:
                print("you win")
                break
    except:
        print("please input a valid number")
    i = i + 1

if i == 10:
    print("you lost")
    print("the number is "+str(myNum))