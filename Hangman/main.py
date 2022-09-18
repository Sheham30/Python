import random

j = 0
guess = ''
words = ["apple", "mango", "banana", "pineapple", "orange", "pear", "grape"]
comp = random.choice(words)

h1 = '''
        O'''
h2 = '''
        O
        |'''
h3 = '''
        O
       \|'''
h4 = '''
        O
       \|/'''
h5 = '''
        O
       \|/
       | '''
h6 = '''
        O
       \|/
       | |'''
hang = [h1, h2, h3, h4, h5, h6]

compList = []
guessList = []

for i in comp:
    compList.append(i)

for i in range(len(comp)):
    guessList.append("-")


def display():
    guessedWord = ""
    for k in guessList:
        guessedWord += k
    return guessedWord


print(f"\n{display()}")
while True:
    if display() != comp:
        guess = input("\nEnter a Guess: ")

        if guess in compList and len(guess) == 1:
            print("Correct")
            r = compList.index(guess)
            guessList[r] = guess
            compList[r] = ""
            print(display())
        elif len(guess) > 1:
            print("invalid choice")
        else:
            print("Incorrect")
            print(hang[j])
            j += 1
            print(display())
            if j == len(hang):
                print("You Lost")
                break
        continue

    print("Congratzzz..You Won")
    break
