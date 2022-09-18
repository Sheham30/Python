board = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}
board_key = []
player = 1
totalmoves = 0
endcheck = 0


def check():
    # checking moves of player1
    if board["1"] == board["2"] == board["3"] == "X":
        print("player1 won")
        return 1
    if board["4"] == board["5"] == board["6"] == "X":
        print("player1 won")
        return 1
    if board["7"] == board["8"] == board["9"] == "X":
        print("player1 won")
        return 1
    if board["1"] == board["4"] == board["7"] == "X":
        print("player1 won")
        return 1
    if board["2"] == board["5"] == board["8"] == "X":
        print("player1 won")
        return 1
    if board["3"] == board["6"] == board["9"] == "X":
        print("player1 won")
        return 1
    if board["1"] == board["5"] == board["9"] == "X":
        print("player1 won")
        return 1
    if board["3"] == board["5"] == board["7"] == "X":
        print("player1 won")
        return 1

    # checking the moves of player2

    if board["1"] == board["2"] == board["3"] == "O":
        print("player2 won")
        return 1
    if board["4"] == board["5"] == board["6"] == "O":
        print("player2 won")
        return 1
    if board["7"] == board["8"] == board["9"] == "O":
        print("player2 won")
        return 1
    if board["1"] == board["4"] == board["7"] == "O":
        print("player2 won")
        return 1
    if board["2"] == board["5"] == board["8"] == "O":
        print("player2 won")
        return 1
    if board["3"] == board["6"] == board["9"] == "O":
        print("player2 won")
        return 1
    if board["1"] == board["5"] == board["9"] == "O":
        print("player2 won")
        return 1
    if board["3"] == board["5"] == board["7"] == "O":
        print("player2 won")
        return 1
    return 0


def tictactoe():
    totalmoves = 0
    player = 1

    r1 = ("1|2|3")
    r2 = "4|5|6"
    r3 = ("7|8|9")

    print(r1)
    print("-+-+-")
    print(r2)
    print("-+-+-")
    print(r3)
    print("\n")

    while True:
        print(board["1"] + "|" + board["2"] + "|" + board["3"])
        print("-+-+-")
        print(board["4"] + "|" + board["5"] + "|" + board["6"])
        print("-+-+-")
        print(board["7"] + "|" + board["8"] + "|" + board["9"])

        endcheck = check()
        if totalmoves == 9 and endcheck == 0:
            print("Game Draw :( ")
            break

        if totalmoves == 9 or endcheck == 1:
            break

        while True:
            if player == 1:
                player1_input = input("Its your turn *PLAYER 1*. Move to which place? ")
                if player1_input in board and board[player1_input] == " ":
                    board[player1_input] = "X"
                    player = 2
                    break
                else:
                    print("Invalid input")
                    continue
            else:
                player2_input = input("Its your turn *PLAYER 2*.. Move to which place? ")
                if board[player2_input] == " ":
                    board[player2_input] = "O"
                    player = 1
                    break
                else:
                    print("Invalid input")
                    continue
        totalmoves += 1


tictactoe()

while True:
    restart = input("Do you want to play again? (y/n) ").lower()
    if restart == "y":
        board = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}
        tictactoe()
    elif restart == "n":
        print("Thanks for playing :)")
        break
    else:
        print("Invalid Choice")