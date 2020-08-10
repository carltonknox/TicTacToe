from TTTGame import rowScan, colScan, firstDiagonalScan, secondDiagonalScan
from itertools import product

def whoseCount(Xcount,Ocount,XO):
    if XO == 'X':
        myCount = Xcount
        theyCount = Ocount
    else:
        myCount = Ocount
        theyCount = Xcount
    return (myCount, theyCount)

def rowSet(board,r,XO):
    for c in range(0,3):
                if board[r][c] ==' ':
                    board[r][c] = XO
                    return

def colSet(board,c,XO):
    for r in range(0,3):
                if board[r][c] == ' ':
                    board[r][c] = XO
                    return

def firstDiagonalSet(board,XO):
    for i in range(0,3):
            if board[i][i] == ' ':
                board[i][i] = XO
                return

def secondDiagonalSet(board,XO):
    for i in range(0,3):
            if board[i][2-i] == ' ':
                board[i][2-i] = XO
                return

def bot(board,XO):
    #winning move checkers
    #row winning move checker
    r = 0
    for row in board:
        Xcount, Ocount = rowScan(row)
        myCount, theyCount = whoseCount(Xcount,Ocount,XO)
        if myCount == 2 and theyCount == 0:
            rowSet(board,r,XO)
            return
        r+=1
    #col winning move checker
    c = 0
    for col in range(0,3):
        Xcount, Ocount = colScan(board,col)
        myCount, theyCount = whoseCount(Xcount,Ocount,XO)
        if myCount == 2 and theyCount == 0:
            colSet(board,c,XO)
            return
        c+=1
    #first diagonal winning move checker
    Xcount, Ocount = firstDiagonalScan(board)
    myCount, theyCount = whoseCount(Xcount,Ocount,XO)
    if myCount == 2 and theyCount == 0:
        firstDiagonalSet(board,XO)
        return
    #second diagonal winning move checker
    Xcount, Ocount = secondDiagonalScan(board)
    myCount, theyCount = whoseCount(Xcount,Ocount,XO)
    if myCount == 2 and theyCount == 0:
        secondDiagonalSet(board,XO)
        return

    #Losing Move Checkers:
    #row losing move checker
    r = 0
    for row in board:
        Xcount, Ocount = rowScan(row)
        myCount, theyCount = whoseCount(Xcount,Ocount,XO)
        if myCount == 0 and theyCount == 2:
            rowSet(board,r,XO)
            return
        r+=1
    #col losing move checker
    c = 0
    for col in range(0,3):
        Xcount, Ocount = colScan(board,col)
        myCount, theyCount = whoseCount(Xcount,Ocount,XO)
        if myCount == 0 and theyCount == 2:
            colSet(board,c,XO)
            return
        c+=1
    #first diagonal losing move checker
    Xcount, Ocount = firstDiagonalScan(board)
    myCount, theyCount = whoseCount(Xcount,Ocount,XO)
    if myCount == 0 and theyCount == 2:
        firstDiagonalSet(board,XO)
        return
    #second diagonal losing move checker
    Xcount, Ocount = secondDiagonalScan(board)
    myCount, theyCount = whoseCount(Xcount,Ocount,XO)
    if myCount == 0 and theyCount == 2:
        secondDiagonalSet(board,XO)
        return

    #Anti Perfect Strategy strategy
    if XO == 'O' and board[1][1] == ' ':
        board[1][1] = XO
        return

    #random moves(corner prioritiy)
    def swap(moves,p1,p2):
        moves[p1],moves[p2] = moves[p2],moves[p1]    
    possibleMoves = list(product(range(0,3),range(0,3)))
    if XO == 'X':#corners for X
        swap(possibleMoves,1,6)
        swap(possibleMoves,3,8)
    else:#sides for O
        swap(possibleMoves,0,5)
        swap(possibleMoves,2,7)
    for r,c in possibleMoves:
        if board[r][c] == ' ':
            board[r][c] = XO
            break