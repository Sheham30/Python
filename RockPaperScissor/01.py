import random
r,p,s = "Rock", "Paper","Scissor"
words = ("Rock", "Paper","Scissor")
cpu = random.choice(words)

me = input("Rock, Paper or Scissor: \n\n")
print(f"{cpu} \n")
if me == cpu:
    print("Game Draw!!")
elif me == "Rock":
    if cpu == "Scissor":
        print("You Won!!")
    elif cpu == "Paper":
        print("You Lost!!")
elif me == "Paper":
    if cpu == "Scissor":
        print("You Lost!!")
    elif cpu == "Rock":
        print("You Won!!")
elif me == "Scissor":
    if cpu == "Paper":
        print("You Won!!")
    elif cpu == "Rock":
        print("You Lost!!")

