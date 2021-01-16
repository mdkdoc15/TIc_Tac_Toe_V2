# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo -- No impact on mac?
    icon = pygame.image.load('Images/icon.png')
    pygame.display.set_icon(icon)
    #Set the name of the window when it pops up
    pygame.display.set_caption("TicTacToe")

     
    # create a surface on screen that has the size of 500 x 500
    SCREEN_SIZE = 500
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

    # Create the storage of the board
    board = ['-','-','-',
        '-','-','-',
        '-','-','-'] #empty game baord

    # Create the main images used for TicTacToe
    x_image = pygame.image.load('Images/x_image.png')
    o_image = pygame.image.load('Images/o_image.png')
    line_image = pygame.image.load('Images/line.png')
    length_of_board_lines = int(SCREEN_SIZE/5*4)
    line_image = pygame.transform.scale(line_image, (length_of_board_lines,20))
    vertical_line_image = pygame.transform.rotate(line_image,90)

    #Drawing for the hashtag that will create the game board
    def base_board():

        buffer_size = int(SCREEN_SIZE/10) # Makes the board not go up to the edge of the window
        spacing_size = int(4*SCREEN_SIZE/5 * (1/3)) # Allows for board to be centered
        screen.blit(line_image, (buffer_size,buffer_size+spacing_size))
        screen.blit(line_image, (buffer_size,buffer_size + 2*spacing_size))
        screen.blit(vertical_line_image, (buffer_size+ spacing_size,buffer_size))
        screen.blit(vertical_line_image, (buffer_size + 2*spacing_size,buffer_size))
    
    def get_loc(pos): # Will return a number 1 - 8, of where the user click, return -1 if an invalid value
        pos_x = pos[0]
        pos_y = pos[1]
        buffer_size = int(SCREEN_SIZE/10) # Makes the board not go up to the edge of the window
        spacing_size = int(4*SCREEN_SIZE/5 * (1/3)) # Allows for board to be centered
        #first checking out of bounds
        if((pos_x or pos_y)< buffer_size or (pos_x or pos_y) > SCREEN_SIZE - buffer_size):
            return -1
        elif((buffer_size <= pos_y  and  pos_y <= buffer_size + spacing_size)):
            # Position is within the first row (0,1,2)
            if((buffer_size <= pos_x  and  pos_x <= buffer_size + spacing_size)):
                return 0
            elif((buffer_size + spacing_size <= pos_x  and  pos_x <= buffer_size + 2* spacing_size)):
                return 1
            else:
                return 2
        elif((buffer_size + spacing_size <= pos_y  and  pos_y <= buffer_size + 2* spacing_size)):
            #Position is within the middle row (3,4,5)
            if((buffer_size <= pos_x  and  pos_x <= buffer_size + spacing_size)):
                return 3
            elif((buffer_size + spacing_size <= pos_x  and  pos_x <= buffer_size + 2* spacing_size)):
                return 4
            else:
                return 5
        else:
            # Position is within the last row (6,7,8)
            if((buffer_size <= pos_x  and  pos_x <= buffer_size + spacing_size)):
                return 6
            elif((buffer_size + spacing_size <= pos_x  and  pos_x <= buffer_size + 2* spacing_size)):
                return 7
            else:
                return 8

    def comp_move():
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

    #Used to update the screen with X's and O's
    def blip_sec(player,loc):
        buffer_size = int(SCREEN_SIZE/10) # Makes the board not go up to the edge of the window
        spacing_size = int(4*SCREEN_SIZE/5 * (1/3)) # Allows for board to be centered
        if(player == 'X'):
            if(loc == 0):
                screen.blit(x_image, (2* buffer_size,2*buffer_size))
            if(loc == 1):
                screen.blit(x_image, (2*buffer_size + spacing_size,2*buffer_size))
            if(loc == 2):
                screen.blit(x_image, (2*buffer_size + 2 * spacing_size,2*buffer_size))
            if(loc == 3):
                screen.blit(x_image, (2*buffer_size,2* buffer_size + spacing_size))
            if(loc == 4):
                screen.blit(x_image, (2*buffer_size + spacing_size,2*buffer_size + spacing_size))
            if(loc == 5):
                screen.blit(x_image, (2*buffer_size + 2 * spacing_size,2*buffer_size + spacing_size))
            if(loc == 6):
                screen.blit(x_image, (2*buffer_size,2*buffer_size + 2 * spacing_size))
            if(loc == 7):
                screen.blit(x_image, (2*buffer_size+ spacing_size ,2*buffer_size + 2 * spacing_size))
            if(loc == 8):
                screen.blit(x_image, (2*buffer_size + 2 * spacing_size,2*buffer_size + 2 * spacing_size))
        else:
            if(loc == 0):
                screen.blit(o_image, (2* buffer_size,2*buffer_size))
            if(loc == 1):
                screen.blit(o_image, (2*buffer_size + spacing_size,2*buffer_size))
            if(loc == 2):
                screen.blit(o_image, (2*buffer_size + 2 * spacing_size,2*buffer_size))
            if(loc == 3):
                screen.blit(o_image, (2*buffer_size,2* buffer_size + spacing_size))
            if(loc == 4):
                screen.blit(o_image, (2*buffer_size + spacing_size,2*buffer_size + spacing_size))
            if(loc == 5):
                screen.blit(o_image, (2*buffer_size + 2 * spacing_size,2*buffer_size + spacing_size))
            if(loc == 6):
                screen.blit(o_image, (2*buffer_size,2*buffer_size + 2 * spacing_size))
            if(loc == 7):
                screen.blit(o_image, (2*buffer_size+ spacing_size ,2*buffer_size + 2 * spacing_size))
            if(loc == 8):
                screen.blit(o_image, (2*buffer_size + 2 * spacing_size,2*buffer_size + 2 * spacing_size))

    def update_board():
        for i in range(0, 9):
            if (board[i] != '-'):
                blip_sec(board[i] , i)
                display_board()

    # Will be used in order to determine if an X needs to be placed
    def mouse_click():
        pos = pygame.mouse.get_pos()
        location = get_loc(pos)
        if(isValidMove(location)):
            board[location] = 'X'
            board[comp_move()] = '0'

    def isValidMove(pos):
        try:
            if (int(pos) > 8 or int(pos) < 0):
                print("Number not allowed (Too Big/Small)")
                return False
            elif (board[int(pos)] != '-'):
                print("Space already taken, try again!")
                return False
            else:
                return True
        except:
            print("Invalid input! Try again!")

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

    # define a variable to control the main loop
    running = True
     
    import os #used to clear screen


    def display_board():
        os.system('clear')#used to clear the screen when drawing a new board
        print(board[0] + ' | ' + board[1] + ' | ' + board[2])
        print(board[3] + ' | ' + board[4] + ' | ' + board[5])
        print(board[6] + ' | ' + board[7] + ' | ' + board[8])


    # main loop
    while running:
        screen.fill((255,255,255)) #Sets the color of the screen to white
        base_board() # Adds the board onto the image
        update_board() # Adds computer and player movements to the screen

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click()
                
        if check_win(board, 'X') or check_win(board, 'O'):
            running = False
        pygame.display.update()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()