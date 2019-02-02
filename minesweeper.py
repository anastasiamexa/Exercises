import random

# Gets the value of a coordinate on the grid.
def l(r, c, b):
    return b[r][c]

# Places a bomb in a random location.
def placeBomb(b):
    r = random.randint(0, row-1)
    c = random.randint(0, column-1)
    # Checks if there's a bomb in the randomly generated location. If not, it puts one there. If there is, it requests a new location to try.
    currentRow = b[r]
    if not currentRow[c] == '*':
        currentRow[c] = '*'
    else:
        placeBomb(b)

# Adds 1 to all of the squares around a bomb.
def updateValues(rn, c, b):
    # Row above.
    if row > (rn - 1) > -1:
        r = b[rn - 1]

        if column > (c - 1) > -1:
            if not r[c - 1] == '*':
                r[c - 1] += 1

        if not r[c] == '*':
            r[c] += 1

        if column > (c + 1) > -1:
            if not r[c + 1] == '*':
                r[c + 1] += 1

    # Same row.
    r = b[rn]

    if column > (c - 1) > -1:
        if not r[c - 1] == '*':
            r[c - 1] += 1

    if column > (c + 1) > -1:
        if not r[c + 1] == '*':
            r[c + 1] += 1

    # Row below.
    if row > (rn + 1) > -1:
        r = b[rn + 1]

        if column > (c - 1) > -1:
            if not r[c - 1] == '*':
                r[c - 1] += 1

        if not r[c] == '*':
            r[c] += 1

        if column > (c + 1) > -1:
            if not r[c + 1] == '*':
                r[c + 1] += 1

# Prints the given board.
def printBoard(b):
    for r in range(0, row):
        list = []
        for c in range(0,column):
            list.append(l(r, c, b))
        print(*list, sep='║')
        if not r == row-1:
            print('══'*len(b))

def tryAgain():
    # This function returns True if the player wants to try again, otherwise it returns False.
    print('Do you want to try again? (yes or no)')
    return input().lower().startswith('y')

# The solution grid.
while True:
    # Input of dimensions
    while True:
        print('Note that columns must be more than rows!!!')
        row = int(input('Enter rows:'))
        column = int(input('Enter column:'))
        if (column > row):
            break
    # Input the number of mines
    while True:
        mines = int(input('Enter the number of mines:'))
        if (mines < row * column):
            break
    b = []
    for j in range(0,column):
        b.append([])
    for i in range(0,row):
        for j in range(0, column):
            b[i].append(j)
            b[i][j] = 0

    for n in range(0, mines):
        placeBomb(b)

    for r in range(0, row):
        for c in range(0, column):
            value = l(r, c, b)
            if value == '*':
                updateValues(r, c, b)
    printBoard(b)
    if not tryAgain():
        break