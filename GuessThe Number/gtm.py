import random
randNumber = random.randint(1, 50)
#print(randNumber)
guesses = 0
userGuess = None
g = 9

while(userGuess != randNumber):
    userGuess = int(input("Enter your Guess: "))
    if(userGuess == randNumber):
        print("\n Congrats!! You guessed it Right!")
        print(f"You guessed the number in {guesses} guesses")
    else:
        if (userGuess > randNumber):
            print("You guessed it Wrong! Enter a SMALLER number..")
        else:
            print("You guessed it Wrong! Enter a LARGER number..")
        if g == 0:
            print("\nYou Lost! \nOut of Guesses")
            break
        print(f"You have {g} guesses left")
        g -= 1
    guesses += 1

