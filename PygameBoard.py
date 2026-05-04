import pygame
import sys
import time
#returns x y coordinates of a specific spot on the board (need to make sure the board stays in the same spot)
def get_board_coordinates(square : str) -> tuple:
     SQUARE_COORDINATES = {
          "a1" : (300,300), 
          "a2" : (300,300), 
          "a3" : (300,300), 
          "a4" : (300,300), 
          "a5" : (300,300), 
          "a6" : (300,300), 
          "a7" : (300,300), 
          "a8" : (300,300), 


     }
     return 200,200


def pygame_board():
    pygame.init()
    WIDTH = 1200
    HEIGHT = 1200
    PIECE_X, PIECE_Y = 50, 50
    running = True
    first = True
    
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Slopfish Chess Engine")
    #colors
    screen_color = (230, 237, 225)
    dark_square_RGB = (116, 152, 174)
    light_square_RGB = (212, 223, 239)
    text_color = (0, 0, 0)
    
    left_board_edge = WIDTH // 4.0
    #left, top, width, height 
    square_size = pygame.Rect(left_board_edge, HEIGHT/4.0, 100, 100) 

    #TODO: Need to figure out this equation to reset the left-most tile, hard code for now

    screen.fill(screen_color)
    #draw numbers/letters
    font = pygame.font.SysFont("monospace", 40)
    column_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    row_names = ['8', '7', '6', '5', '4', '3', '2', '1']
    print_helper = 325
    #draw tiles
    for i in range(8):
        for j in range(4):
            if i % 2 == 0:   
                pygame.draw.rect(screen, dark_square_RGB, square_size)
                square_size.centerx += 80
                pygame.draw.rect(screen, light_square_RGB, square_size)
                square_size.centerx += 80
            else:
                pygame.draw.rect(screen, light_square_RGB, square_size)
                square_size.centerx += 80
                pygame.draw.rect(screen, dark_square_RGB, square_size)
                square_size.centerx += 80
        #print ranks
        current_number = font.render(row_names[i], 0, text_color)
        screen.blit(current_number, (left_board_edge - 25, print_helper))
        #print files
        current_rank = font.render(column_names[i], 0, text_color)
        screen.blit(current_rank, (print_helper, 950))
        #move over squares
        print_helper += 80
        square_size.centery += 80
        square_size.centerx = left_board_edge + (square_size.width / 2)



    #load initial pieces 
    black_bishop1 = pygame.image.load('pieceImages/bB.svg').convert_alpha()
    black_bishop2 = pygame.image.load('pieceImages/bB.svg').convert_alpha()

    black_bishop1 = pygame.transform.smoothscale(black_bishop1, (PIECE_X, PIECE_Y))
    black_bishop2 = pygame.transform.smoothscale(black_bishop2, (PIECE_X, PIECE_Y))

    screen.blit(black_bishop1, (315, 315))
    screen.blit(black_bishop2, get_board_coordinates(" HI"))

    while running:
        #do these need to run in the loop?
        #pygame.display.set_mode([WIDTH, HEIGHT])
        #pygame.display.set_caption("Chess Board")

        #boolean flag to check success of opening board
        if first:
            if pygame.get_init():
                    print("Board opened successfully")
                
            else:
                    RuntimeError("Failure to load board")
                    
            first = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        pygame.display.flip()

    pygame.quit()
    return
