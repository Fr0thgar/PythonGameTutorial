# Pygame development 1
# start the basic game set up
# set up the display

# gain access to the pygame library
import pygame

# sizee of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# colors according to RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()
TICK_RATE = 60
is_game_over = False

# create the window of specified size in white to display the game
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# set the game window color to white
game_screen.fill(WHITE_COLOR)


while not is_game_over:

    

    pygame.display.update()
    clock.tick(TICK_RATE)
