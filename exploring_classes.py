
# today, my goal is to explore classes and make collectibles that appear randomly on the screen and move from the right side of the screen to the left
# later, these colletibles will be represented as sprites, but, for now, I'm just going to draw some shapes on the screen and work on the fundamental logic
import pygame 
from pygame.locals import *
from sys import exit
from random import randint

# defining my screen's measures
length = 860
width = 640 
screen = pygame.display.set_mode((length, width))

# creating the player
player_x = 0
player_y = 0

# creating the collectible's class

class Collectible:

    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw_collec(self):

        pygame.draw.circle(screen, lilac, (self.x_pos, self.y_pos), 100)

    # def movement(self):
    #     x_pos += 1
    #     if x_pos >= length:
    #         x_pos = 0

# naming some RGB tuples 
black = (0, 0, 0)
white = (255, 255, 255)
light_green = (128, 200, 128)
pink = (255, 0, 255)
lilac = (200, 162, 200)

while True:

    # screen.fill(light_green)
    pygame.display.flip()

    # drawing the collectible

    collec_1 = Collectible(width//2, length//2)
    collec_1.draw_collec()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # controlling the player

    if pygame.key.get_pressed()[K_w]:

        player_y -= 10

    if pygame.key.get_pressed()[K_s]:

        player_y += 10

    if pygame.key.get_pressed()[K_d]:

        player_x += 10

    if pygame.key.get_pressed()[K_a]:

        player_x -= 10

    # drawing the player
    pygame.draw.rect(screen, pink, (player_x, player_y))



    

        






        




