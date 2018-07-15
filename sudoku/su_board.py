#Find next empty cell
def findNextCell(board):
     for i in xrange (0, 9):
        for j in xrange (0, 9):
            if(board[i][j] == 0):
                return [i, j]

#Check board is full value
def isFull(board):
    for i in xrange(0,9):
        for j in xrange(0,9):
            if(board[i][j] == 0): return False
    return True

#Check cell valid
def isValid(board, row, col, v): 
    for c in xrange(0, 9):
        if(board[row][c] == v): return False
    for r in xrange(0, 9): 
        if(board[r][col] == v): return False

    for r in xrange (0, 3):
        for c in xrange (0, 3):
            if(board[r + (row-row%3)][c + (col-col%3)] == v): return False
    return True

#Check board contain invalid value
def verifyBoard(board):
    boardRow = len(board)
    if(boardRow != 9): return False
    boardCol = len(board[0])
    if(boardCol != 9): return False

    for r in xrange(0, 9):
        for c in xrange(0, 9):
            v = board[r][c]
            if(v>0):
                board[r][c] = 0
                if(isValid(board, r, c, v) == False):
                    board[r][c] = v
                    return False
    return True

#Find solution
def sudokuSol(board):
    if(isFull(board)):
        return True

    [i, j] = findNextCell(board)
    for v in xrange(1, 10):
        if(isValid(board, i, j, v)):
            board[i][j] = v
            if(sudokuSol(board) == True): 
                return True
            board[i][j] = 0
    
    return False

#Solve full step
def solveSDKBoard(board):
    #Verify board
    if(verifyBoard(board)):
        #Find sol
        return sudokuSol(board)
    return False

suBoard1 = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

suBoard2 = [[0, 9, 0, 0, 0, 0, 8, 5, 3],
            [0, 0, 0, 8, 0, 0, 0, 0, 4],
            [0, 0, 8, 2, 0, 3, 0, 6, 9],
            [5, 7, 4, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 9, 0, 0, 6, 3, 7],
            [9, 4, 0, 1, 0, 8, 5, 0, 0],
            [7, 0, 0, 0, 0, 6, 0, 0, 0],
            [6, 8, 2, 0, 0, 0, 0, 9, 0]]


print('input', suBoard2)
if(solveSDKBoard(suBoard2) == True):
    print('output', suBoard2)
else:
    print('no solution')




