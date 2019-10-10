# Pygame development 1 - 4
# start the basic game set up
# set up the display

# gain access to the pygame library
import pygame

# sizee of the screen
SCREEN_TITLE = 'Crossy RPG'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# colors according to RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
#clock used to update game events and frames
clock = pygame.time.Clock()

class Game:
    
    # typical rate of 60, equivalent to FPS
    TICK_RATE = 60
    
    # initializer for the game class to set up the width, height, and title
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        # create the window of specified size in white to display the game
        game_screen = pygame.display.set_mode((width, height))
        # set the game window color to white
        game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)
        
    def run_game_loop(self):
        is_game_over = False

        # main game loop , used to update all gameplay such as movement, checks, and graphiccs
        # Runs until is_game_over = True
        while not is_game_over:

            # aloop to get all of the events occuring at any given time
            # events are most often mouse movement, mouse and button clicks, or exit events
            for event in pygame.event.get():
                # if we have quit type event (exit out) then exit out of the game loop
                if event.type == pygame.QUIT:
                    is_game_over = True
                    
                print(event)

            

            #update all game graphics
            pygame.display.update()
            # tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)
        

pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()




# quit pygame and the program
pygame.quit()
quit()


# draw a rectangle on top of the game screen canvas(x, y, width, height)
            #    pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
            # draw a circle on top of the game screen canvas( x, y, radius)
            #    pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

            #game_screen.blit(player_image, (375, 375))


# load the player image from the file directory
#player_image = pygame.image.load('player.png')
#scale the image up
#player_image = pygame.transform.scale(player_image, (50, 50))