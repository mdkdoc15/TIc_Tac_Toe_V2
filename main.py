#First attempt at basic AI
#ideas from https://www.youtube.com/watch?v=jAaJZLqryTI&t=9s

import os #used to clear screen


def display_board(board):
    os.system('clear')#used to clear the screen when drawing a new board
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def isValidMove(board,pos):
    try:
        if (int(pos) > 9 or int(pos) < 1):
            print("Number not allowed (Too Big/Small)")
            return False
        elif (board[int(pos)-1] != '-'):
            print("Space already taken, try again!")
            return False
        else:
            return True
    except:
        print("Invalid input! Try again!")

def selectRandom(list_of_vals):
    import random as rand
    length = len(list_of_vals)
    r = rand.randrange(0, length)
    return list_of_vals[r]

def compMove(board):
    # #----------
    # Order is determined by:
    # Way to win
    # Way to stop a win 
    # Pick the center
    # Pick random corner
    # Pick random available piece
    # #----------
    possibleMoves = [x for x, letter in enumerate(board) if letter == '-'] #creates a list all the empty spaces
    if len(possibleMoves) > 0: #if there is an open space
        for letter in ['O', 'X']:
            for i in possibleMoves:
                boardCopy = board[:] #creates a copy of the board to check if there was a win at each possible position
                boardCopy[i] = letter
                if check_win(boardCopy, letter):
                    return i

        if 4 in possibleMoves: #return the center if found
            return 4
        
        cornersOpen =[] #If there is not an immeditate win then find a corner to place in
        for i in possibleMoves: #Find if the corners are available from the list of open spots
            if i in [0,2,6,8]:
                cornersOpen.append(i) #add them to the list if found
        if len(cornersOpen) > 0: #if there was an open corner
            return selectRandom(cornersOpen)

        return(selectRandom(possibleMoves)) #if this pointed is reached then all possible moves left are edges, pick one at random
    
    else: #if there is no open spaces return -1
        return -1 

def handle_turn(board,player):
   
        if(player): #Will alternate players based on the state of the boolean 'player'
             while True:
                position = input("Choose a position from 1-9: ")
                if(isValidMove(board,position)):
                    board[int(position)-1] = 'X'
                    if(check_win(board, 'X')):
                        display_board(board)
                        print("You won! Good Job!")
                    break
        else:
            move = compMove(board)
            if move >= 0 :
                board[move] = 'O'
                if(check_win(board, 'O')):
                    display_board(board)
                    print('The computer won this time. Try again?')
            else:
                display_board(board)
                print("Tie game! Try again?")

    
def check_col(board , player):
    #find better way to do this
    if(board[0] == board[3] == board[6] == player):
        return True
    if(board[1] == board[4] == board[7] == player):
        return True
    if(board[2] == board[5] == board[8] == player):
        return True
    return False

def check_row(board , player):
    #find better way to do this
    if(board[0] == board[1] == board[2] == player):
        return True
    if(board[3] == board[4] == board[5] == player):
        return True
    if(board[6] == board[7] == board[8] == player):
        return True
    return False

def check_diag(board , player):
    if(board[0] == board[4] == board[8] == player):
        return True
    if(board[2] == board[4] == board[6]== player):
        return True
    return False

def check_tie(board):
    for i in board:
        if(i == '-'):
            return False
    display_board(board)
    print("Tie game!")
    return True

def check_win(board , player):
    return check_diag(board , player) or check_col(board , player) or check_row(board , player)


def play_game():
    board = ['-','-','-',
        '-','-','-',
        '-','-','-'] #empty game baord
    game_over = False
    player = True #true players are X, false are O's
    while(not game_over):
        display_board(board) #print the board at the start of each turn
        handle_turn(board,player)
        player = not player # move to next persons turn
        game_over = (check_win(board, 'X') or check_win(board, 'O') or check_tie(board)) #determines if we need to exit the loop
        

while True:
    play = input("Would you like to play TicTacToe(Y/N)")
    if(play == 'N'):
        break
    else:
        play_game()
