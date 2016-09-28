def explain_board():
    b = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]
    return b

def new_board():
    b = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    return b

def is_winner(player, board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:  #check rows
            return True
        elif board[0][i] == board[1][i] == board[2][i] == player: #check cols
            return True
    if board[0][0] == board[1][1] == board[2][2] == player: #check diags
        return True
    elif board[0][2] == board[1][1] == board[2][0] == player:
        return True
    else:
        return False

def is_full(board):
    for i in board:
        for s in i:
            if s == " ":
                return False
    return True 

def display(board):
    v = " | "
    m = "\t\t"
    print "\n" + m + board[0][0] + v + board[0][1] + v + board[0][2]
    print m + "---------"
    print m + board[1][0] + v + board[1][1] + v + board[1][2]
    print m + "---------"
    print m + board[2][0] + v + board[2][1] + v + board[2][2] + "\n"

def check_validity(move, board):
    moves = {
        "1": board[0][0], 
        "2": board[0][1],
        "3": board[0][2],
        "4": board[1][0],
        "5": board[1][1],
        "6": board[1][2],
        "7": board[2][0],
        "8": board[2][1],
        "9": board[2][2]
    }
    if move in moves:
        if moves[move] == " ":
            return True
    else:
        return False

def play_move(player, board, move):
    if check_validity(move, board):
        if move == "1": 
            board[0][0] = player 
        elif move == "2": 
            board[0][1] = player
        elif move == "3": 
            board[0][2] = player
        elif move == "4": 
            board[1][0] = player
        elif move == "5": 
            board[1][1] = player
        elif move == "6": 
            board[1][2] = player
        elif move == "7": 
            board[2][0] = player
        elif move == "8": 
            board[2][1] = player
        elif move == "9":
            board[2][2] = player
        return board 
    else:
        print "That is not a valid move. Please try again. [1-9]"
        return play_move(player, board, raw_input("> "))
    
def change_player(player):
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return player

def explain():
    print "The grid has nine numbered spaces: "    
    display(explain_board())
    print "X to play first.\n"
    
def tic_tac_toe():
    explain()
    board = new_board()
    player = "O"
    while not(is_winner(player, board) or is_full(board)):
        player = change_player(player)
        print player + ", where would you like to play? [1-9]"
        board = play_move(player, board, raw_input("> "))
        display(board)
    
    if is_winner(player, board):
        print "The game is a win for " + player + "."
    else:
        print "The game is a tie."


if __name__ == "__main__":
    tic_tac_toe()
