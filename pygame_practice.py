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
        

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        screen.fill((255,255,255)) #Sets the color of the screen to white
        base_board()
        pygame.display.update()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()