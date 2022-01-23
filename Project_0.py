xoxBoard = [['-', '-', '-',], ['-', '-', '-',], ['-', '-', '-',]]
def print_board():
    a = 0
    print("                                           0   1   2")
    for row in xoxBoard:
        print("                                         ", end="")
        for collumn in row:
            if collumn == '-':
                print('|   ', end='')
            else:
                print(f"| {collumn} ", end='')
        print(f"|{a}\r")   
        a += 1

def display_player_scores(p1, p2):
    print(f"                            PLAYER 1: {p1}                  PLAYER 2: {p2}")

def legal_moves():
    legalMoves = []
    rowNum = 0
    collumnNum = 0
    for row in xoxBoard:
        collumnNum = 0
        for collumn in row:
            if collumn == '-':
                legalMoves.append(f'[{collumnNum}][{rowNum}]')
            collumnNum += 1
        rowNum += 1
    return legalMoves


def make_a_move(p1,p2):
    playerInTurn = p1
    ls = legal_moves()
    print(f"{playerInTurn}'s turn, make a move:")
    for a in range(len(ls)):
        print(f"{a}) {ls[a]}")
    move = input()

def start_game():
    print("Hello! Welcome to our game, Tic Tac Toe.")
    enter = input("Press enter to continue.")
    print("\n"*27)
    print("Rules for the game:\nThere will be two players, one playing X and the other one O.\n\nThe player has to get three in a row, whether it being horizontal, vertical or diagonal.\n\nThe moves you can play are written as [collumn number][row number].\n")
    print("Have fun playing!")
    enter = input("Press enter to continue.")
    print("\n"*27)
    print("\n"*20)

def isTerminal():
    if xoxBoard[0][0] == xoxBoard[0][1] and xoxBoard[0][0] == xoxBoard[0][2]:
        return True
    elif xoxBoard[0][1] == xoxBoard[1][1] and xoxBoard[0][1] == xoxBoard[2][1]:
        return True
    elif xoxBoard[0][2] == xoxBoard[1][2] and xoxBoard[0][2] == xoxBoard[2][2]:
        return True
    elif xoxBoard[0][0] == xoxBoard[1][0] and xoxBoard[0][0] == xoxBoard[2][0]:
        return True
    elif xoxBoard[1][0] == xoxBoard[1][1] and xoxBoard[1][0] == xoxBoard[1][2]:
        return True
    elif xoxBoard[2][0] == xoxBoard[2][1] and xoxBoard[2][0] == xoxBoard[2][2]:
        return True
    elif xoxBoard[0][0] == xoxBoard[1][1] and xoxBoard[0][0] == xoxBoard[2][2]:
        return True
    elif xoxBoard[0][2] == xoxBoard[1][1] and xoxBoard[0][2] == xoxBoard[2][0]:
        return True
    else:
        return False
    

def main():
    start_game()
    playerX = 0
    playerO = 0
    display_player_scores(playerX, playerO)

    print_board()

    make_a_move(playerX, playerO)

    
main()
