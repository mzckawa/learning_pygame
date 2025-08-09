
# today, my goal is to explore classes and make collectibles that appear randomly on the screen and move from the right side of the screen to the left
# later, these colletibles will be represented as sprites, but, for now, I'm just going to draw some shapes on the screen and work on the fundamental logic
import pygame 
from pygame.locals import *
from sys import exit
from random import randint

# defining my screen's measures
width = 860
height = 640 
screen = pygame.display.set_mode((width, height))


# creating the player
player_x = 0
player_y = 0

# creating the collectible's class

class Collectible:

    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = pygame.Rect(self.x_pos, self.y_pos, 100, 100)
        self.collected = False

    def draw_collec(self):
        pygame.draw.rect(screen, lilac, self.rect)

    def movement(self):
        self.x_pos -= 10
        if self.x_pos <= 0:
            self.x_pos = width
        self.rect = pygame.Rect(self.x_pos, self.y_pos, 100, 100)

# naming some RGB tuples 
black = (0, 0, 0)
white = (255, 255, 255)
light_green = (128, 200, 128)
pink = (255, 0, 255)
lilac = (200, 162, 200)

# creating the first collectible 

x_collect = randint()
collec_1 = Collectible(width//2, height//2)

# creating a clock

clock = pygame.time.Clock()

while True:

    clock.tick(30)

    screen.fill(light_green) 

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # controlling the player

    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:

        player_y -= 10

    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:

        player_y += 10

    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:

        player_x += 10

    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:

        player_x -= 10

    # drawing the player
    player = pygame.draw.rect(screen, pink, (player_x, player_y, 100, 100))

    # drawing the collectible
    if not collec_1.collected:
        collec_1.draw_collec()
        collec_1.movement()

    # creating the collision conditional
    if player.colliderect(collec_1):
        collec_1.collected = True


    pygame.display.flip()
    


    

        






        




