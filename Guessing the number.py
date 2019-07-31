# simple game to guess a number 1-20
import random
print("Hello what is your name?")
name = input()
print("Well, " + name + " lets play a game\n")
# This is where a number is generated
secretNum = random.randint(1, 20)
# the total number of trys is defined as six because in the for loop one is subtracted
totaltry = 6
for Numguess in range(1, 6):
    totaltry -= 1
    print("Guess the number you have " + str(totaltry) + " try's left in the game")
# This is a valudation check to make sure input is a number
    try:
        guess = int(input())
    except ValueError:
        print("This is not a number!")
        continue
    if guess < secretNum:
        print("your guess is too low!")
    elif guess > secretNum:
        print("your guess to too high!")
    # if the number is guessed right it will break from code and print
    else:
        break

if guess == secretNum:
    print("Good job, " + name + " you guessed the right num!")
# if all the ties are used then this is the outcome
else:
    print("Too many tries play again")