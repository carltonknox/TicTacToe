def scanTie(board):
    return not any(' ' in row for row in board)

def rowScan(row):
    Xcount = 0
    Ocount = 0
    for XO in row:
        if XO == 'X':
            Xcount+=1
        elif XO == 'O':
            Ocount+=1
    return (Xcount,Ocount)

def colScan(board,col):
    Xcount = 0
    Ocount = 0
    for row in range(0,3):
        XO = board[row][col]
        if XO == 'X':
            Xcount+=1
        elif XO == 'O':
            Ocount+=1
    return (Xcount,Ocount)

def firstDiagonalScan(board):
    Xcount = 0
    Ocount = 0
    for XO in [board[i][i] for i in range(0,3)]:
        if XO == 'X':
            Xcount+=1
        elif XO == 'O':
            Ocount+=1
    return (Xcount,Ocount)

def secondDiagonalScan(board):
    Xcount = 0
    Ocount = 0
    for XO in [board[i][2-i] for i in range(0,3)]:
        if XO == 'X':
            Xcount+=1
        elif XO == 'O':
            Ocount+=1
    return (Xcount, Ocount)
def scanWin(board):
    #Horizontal Row Check
    for row in board:
        Xcount, Ocount = rowScan(row)
        if Xcount == 3 or Ocount == 3:
            return True
    #Vertical Column Check
    for col in range(0,3):
        Xcount, Ocount = colScan(board,col)
        if Xcount == 3 or Ocount == 3:
            return True
    #1st diagonal check
    Xcount, Ocount = firstDiagonalScan(board)
    if Xcount == 3 or Ocount == 3:
            return True
    #2nd Diagonal Check
    Xcount, Ocount = secondDiagonalScan(board)
    if Xcount == 3 or Ocount == 3:
            return True
    
    return False