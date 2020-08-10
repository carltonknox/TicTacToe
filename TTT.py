import TTTIO
import TTTGame
import TTTBOT
def main():
    board = [
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']
        ]
    XO='O'
    print("Single Player or Two Player?")
    st = input("Players (1 or 2): ")
    if st in ('2','t'):
        #Two Player:
        print("Let's Play some Tic Tac Toe!:\n")
        TTTIO.TTTO(board)
        while True:
            if TTTGame.scanWin(board):
                print(f"Player {XO} Wins!!!")
                break
            if TTTGame.scanTie(board):
                print("It's a Tie!")
                break
            if XO == 'X':
                XO = 'O'
            else:
                XO = 'X'
            print(f"Player {XO}:")
            TTTIO.TTTI(board,XO)
            TTTIO.TTTO(board)
    
    elif st in ('1','s'):
        playerXO = input("Would you like to play as 'X' or 'O'?: ")
        print("Let's Play some Tic Tac Toe!:\n")
        TTTIO.TTTO(board)
        while True:
            if TTTGame.scanWin(board):
                print(f"Player {XO} Wins!!!")
                break
            if TTTGame.scanTie(board):
                print("It's a Tie!")
                break
            if XO == 'X':
                XO = 'O'
            else:
                XO = 'X'
            print(f"Player {XO}:")
            if XO == playerXO:
                TTTIO.TTTI(board,XO)
                TTTIO.TTTO(board)
            else:
                TTTBOT.bot(board,XO)
                TTTIO.TTTO(board)

    elif st in ('0','n'):
        print("Let's NOT Play some Tic Tac Toe!:\n")
        TTTIO.TTTO(board)
        while True:
            if TTTGame.scanWin(board):
                print(f"Player {XO} Wins!!!")
                break
            if TTTGame.scanTie(board):
                print("It's a Tie!")
                break
            if XO == 'X':
                XO = 'O'
            else:
                XO = 'X'
            TTTBOT.bot(board,XO)
            TTTIO.TTTO(board)
            print()


    else:
        print("so no game? okay I guess...")


if __name__ == "__main__":
    main()