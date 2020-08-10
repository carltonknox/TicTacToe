def TTTO(board):
    c=0
    for row in board:
        r = 0
        for XO in row:
            print(f"{XO} ",end='')
            if r < 2:
                print("| ",end='')
            else:
                print()
            r+=1

        if c < 2:
            print("---------")
        c+=1

def TTTI(board,XO):
    done = False
    while not done:
        temp_board = board[:]
        print("Please enter the row and column")
        r = int(input("r: "))
        c = int(input("c: ")) 
        if r not in range(0,3) or c not in range(0,3):
            print("Error: out of range")
            continue
        if board[r][c] != ' ':
            print('space already occupied!')
            continue
        temp_board[r][c] = '?'
        print("Is this correct?")
        TTTO(temp_board)
        correct=input("y/n: ")
        if correct=='y':
            done = True
            board[r][c] = XO
        else:
            temp_board[r][c] = ' '

    