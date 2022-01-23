xoxBoard = [['-', '-', '-',], ['-', '-', '-',], ['-', '-', '-',]]
xoxBoard[0][2] = 'X'
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

def isTerminal():
    # TODO: Check if there are back to back X's or O's
    pass
    if xoxBoard[0][0] == xoxBoard[0][1] and xoxBoard[0][0] == xoxBoard[0][2]:
        return True
    elif xoxBoard[0][1] == xoxBoard[1][1] and xoxBoard[0][1] == xoxBoard[2][1]:
        return True
    elif xoxBoard[0][2] == xoxBoard[1][2] and xoxBoard[0][2] == xoxBoard[2][2]:
        return True
    elif xoxBoard[0][0] == xoxBoard[1][0] and xoxBoard[0][0] == xoxBoard[2][0]:
        return True
    

def main():
    player1_score = 0
    player2_score = 0
    display_player_scores(player1_score, player2_score)

    print_board()

    make_a_move(player1_score, player2_score)

    
main()