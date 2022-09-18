def displayMatrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    for r in range(rows):
        for c in range(columns):
            print("%10.3f" % (matrix[r][c]), end="\t")
        print()
    print()


def inputMatrix():
    nr = int(input("Enter Number of rows :"))
    nc = int(input("Enter Number of columns :"))

    matrix = []
    for r in range(nr):
        row = []
        for c in range(nc):
            element = float(input("Enter element M(," + str(r + 1) + "," + str(c + 1) + ") :"))
            row.append(element)
        matrix.append(row)
    return matrix


def reduceToOne(matrix, pivotRow, pivotColumn):
    numberOfCols = len(matrix[0])
    pivotElement = matrix[pivotRow][pivotColumn]
    for j in range(numberOfCols):
        matrix[pivotRow][j] = matrix[pivotRow][j] / pivotElement
    return matrix


def reduceToZero(matrix, pivotRow, pivotColumn):
    numberOfRows = len(matrix)
    numberOfColumns = len(matrix[0])

    for r in range(numberOfRows):
        if (r != pivotRow):
            makeZero = matrix[r][pivotColumn]
            for j in range(numberOfColumns):
                matrix[r][j] = matrix[r][j] - makeZero * matrix[pivotRow][j]
    return (matrix)

# -------------------- Main program ------------------------


def solve(mat):
    displayMatrix(mat)
    for pr in range(len(mat)):
        for pc in range(len(mat)):
            if pr == pc:
                mat = reduceToOne(mat, pr, pc)

                mat = reduceToZero(mat, pr, pc)

    displayMatrix(mat)


sd = [[1, 1, 2, 9], [2, 4, -3, 1], [3, 6, -5, 0]]
solve(sd)