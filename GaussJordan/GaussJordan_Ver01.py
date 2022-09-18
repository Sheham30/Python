# r = int(input("Enter number of rows"))
# c = int(input("Enter number of columns"))
sd = [[1, 1, 2, 9], [2, 4, -3, 1], [3, 6, -5, 0]]


# for i in range(r):
#     sd2 = []
#     for j in range(c):
#         x = input(f"Enter {i+1}, {j+1}: ")
#         sd2.append(x)
#     sd.append(sd2)

def displayMatrix(mat):
    print("")
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end="\t\t")
        print("")

nr = 3
nc = 4
displayMatrix(sd)

pr = int(input("Enter row of pivot element: "))
pc = int(input("Enter column of pivot element: "))

while (pr > 0) and (pc > 0):
    pr -= 1
    pc -= 1
    pe = sd[pr][pc]

    for i in range(nc):
        sd[pr][i] = sd[pr][i]/pe

    for r in range(nr):
        if r != pc:
            makeZero = sd[r][pc]
            for c in range(4):
                sd[r][c] = sd[r][c] - (makeZero * sd[pr][c])

    displayMatrix(sd)
    pr = int(input("Enter row of pivot element: "))
    pc = int(input("Enter row of pivot element: "))


