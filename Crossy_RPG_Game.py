# Pygame development 7
# Implement game classes
# implement generic game objevct class

# gain access to the pygame library
import pygame

# sizee of the screen
SCREEN_TITLE = 'Crossy RPG'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# colors according to RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
# clock used to update game events and frames
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
        self.game_screen = pygame.display.set_mode((width, height))
        # set the game window color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False
        direction = 0

        player_character = PlayerCharacter('player.png', 375, 700, 50, 50)
        enemy_0 = NonPlayerCharacter('enemy.png', 20, 400, 50, 50)
        # main game loop , used to update all gameplay such as movement, checks, and graphiccs
        # Runs until is_game_over = True
        while not is_game_over:

            # aloop to get all of the events occuring at any given time
            # events are most often mouse movement, mouse and button clicks, or exit events
            for event in pygame.event.get():
                # if we have quit type event (exit out) then exit out of the game loop
                if event.type == pygame.QUIT:
                    is_game_over = True
                    # Detects when key is pressed down
                elif event.type == pygame.KEYDOWN:
                    # move up if up key pressed
                    if event.key == pygame.K_UP:
                        direction = 1
                    # move down if down key pressed
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # detect when key is released
                elif event.type == pygame.KEYUP:
                    # stop movement when key no longer pressed
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)

            # redraw the screen to be a blank white window
            self.game_screen.fill(WHITE_COLOR)
            # update the player position
            player_character.move(direction, self.height)
            # draw the player at the new position
            player_character.draw(self.game_screen)

            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            # update all game graphics
            pygame.display.update()
            # tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)


class GameObject:

    def __init__(self, image_path, x, y, width, height):
        # load the player image from the file directory
        object_image = pygame.image.load(image_path)
        # scale the image up
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

# class to represent the character controlled by the player


class PlayerCharacter(GameObject):

    # how many tiles the character moves per second
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # move function will move character up if direction > 0 and down if < 0
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40
        elif self.y_pos <= max_height - 770:
            self.y_pos = max_height - 770

class NonPlayerCharacter(GameObject):

    # how many tiles the character moves per second
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # move function will move character up if direction > 0 and down if < 0
    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED


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
# scale the image up
#player_image = pygame.transform.scale(player_image, (50, 50))
