
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
player_x = 20
player_y = 2 * height//3

# creating the collectible's class

class Collectible:

    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.collected = False
        self.lost = False

    def draw_collec(self):
        pygame.draw.rect(screen, lilac, self.rect)

    def movement(self):

        self.x_pos -= 10

        if self.x_pos < -2 * self.width: # in order to make the collectible disappear from the screen, but stop being drawn
            self.lost = True

        else:
            self.rect = pygame.Rect(self.x_pos, self.y_pos, 50, 50) # if we do this command under the condition of the o

# naming some RGB tuples 
black = (0, 0, 0)
white = (255, 255, 255)
light_green = (128, 200, 128)
pink = (255, 0, 255)
lilac = (200, 162, 200)

# defining a random number of appearances for the collectibles 
amount_collect = randint(1, 10)

# creating a dictionary to store the collectibles with their positions
collects_1_dic = {}
dic_collec_1_collected = {} # to store the collectibles that were collected
dic_collec_1_lost = {} # to store the collectibles that exceed the screen size without being caught by the player

for i in range(amount_collect):

    # generating random positions for the collectibles 
    x_collect = randint(player_x * 2, width) - 100
    y_collect = randint(height//2, height) - 100

    # creating the objects of the class Collectible with the generated random positions
    collects_1_dic[i] = Collectible(x_collect, y_collect)

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

    # drawing the collectibles

    for i in range(amount_collect):

        # creating the collision conditional
        if player.colliderect(collects_1_dic[i]):
            if player.colliderect(collects_1_dic[i]):
                collects_1_dic[i].collected = True

        # keeping on drawing the collectible, if it was not caught by the player 
        if not collects_1_dic[i].collected:
            collects_1_dic[i].draw_collec()
            collects_1_dic[i].movement()

            # if the x position of the collectible is lesser than 0, it means the player didn't catch it, so it's lost
            if collects_1_dic[i].lost:
                dic_collec_1_lost[i] = collects_1_dic[i]

    pygame.display.flip()
