import pygame
import sys
import time
def pygame_board():
    pygame.init()
    WIDTH = 1080
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
    text_color = (209, 209, 209)
    
    left_board_edge = WIDTH // 4.0
    #left, top, width, height 
    square_size = pygame.Rect(left_board_edge, HEIGHT/4.0, 80, 80) 

    #TODO: Need to figure out this equation to reset the left-most tile, hard code for now

    screen.fill(screen_color)

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

        square_size.centery += 80
        square_size.centerx = left_board_edge + (square_size.width / 2)


    #draw numbers/letters
    font = pygame.font.SysFont("monospace", 40)
    column_names = ['a', 'b', 'c', 'd', 'e', 'f']
    row_names = ['8', '7', '6', '5', '4', '3', '2', '1']
    print_helper = 300
    #printing rows
    for i in range(8):
        current_number = font.render(row_names[i], 0, text_color)
        screen.blit(current_number, (left_board_edge - 25, print_helper))
        print_helper += 80
  

    #load initial pieces 
    black_bishop = pygame.image.load('pieceImages/bB.svg').convert_alpha()
    black_bishop = pygame.transform.smoothscale(black_bishop, (PIECE_X, PIECE_Y))

    screen.blit(black_bishop, (200, 200))

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
