
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
        self.adequate_distance = False # to help verifying whether the collectibles are not too close or overlapping each other

    def draw_collec(self):
        pygame.draw.rect(screen, lilac, self.rect)

    def movement(self):

        self.x_pos -= 10

        if self.x_pos < -2 * self.width: # in order to make the collectible disappear from the screen, but stop being drawn
            self.lost = True

        else:
            self.rect = pygame.Rect(self.x_pos, self.y_pos, 50, 50) # if we do this command under the condition of the o

def Closeness(list):

    global height
    y = randint(height//2, height) - 30

    if list:

        for i in range(len(list)):

            if abs(y_pos_collects_1[i] - y_pos_collects_1[-1]) < 20:
                y = randint(height//2, height) - 30
                return Closeness

    return y

# naming some RGB tuples
black = (0, 0, 0)
white = (255, 255, 255)
light_green = (128, 200, 128)
pink = (255, 0, 255)
lilac = (200, 162, 200)

# defining a random number of appearances for the collectibles
amount_collect = randint(1, 10)

# creating a list list to store the collectibles more easily
all_collects_1 = []
y_pos_collects_1 = []

for i in range(amount_collect):

    x_collect = width # we want the collectibles to always go from the right side to the left side
    y_collect = Closeness(y_pos_collects_1)  # generating a random y-axis position for the collectibles that is not too close from the previous ones

    # adding the random-yet-adequate y-axis position to the list of positions
    y_pos_collects_1.append(y_collect)

    # creating the objects of the class Collectible with the generated random positions
    collectible = Collectible(x_collect, y_collect)

    # adding the newly-created collectible to the list with the other collectibles of the same kind
    all_collects_1.append(collectible)

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

    # adding the collectibles to the list with all the collectibles of the same type



    # drawing the collectibles based on which of them were already collected or lost

    remaining_collect_1 = []

    for collectible in all_collects_1:

        # creating the collision conditional
        if player.colliderect(collectible):
            if player.colliderect(collectible):
                collectible.collected = True

        # keeping on drawing the collectible, if it was not caught by the player
        if not collectible.collected:
            collectible.draw_collec()
            collectible.movement()

        if not collectible.collected and not collectible.lost:

            remaining_collect_1.append(collectible)

    # recreating the list of all collectibles only with the ones actually available
    all_collects_1 = remaining_collect_1

    if not all_collects_1: # let's go all over again!

        # defining a random number of appearances for the collectibles
        amount_collect = randint(1, 10)

        for i in range(amount_collect):

            x_collect = width # we want the collectibles to always go from the right side to the left side
            y_collect = Closeness(y_pos_collects_1)  # generating a random y-axis position for the collectibles that is not too close from the previous ones

            # adding the random-yet-adequate y-axis position to the list of positions
            y_pos_collects_1.append(y_collect)

            # creating the objects of the class Collectible with the generated random positions
            collectible = Collectible(x_collect, y_collect)

            # adding the newly-created collectible to the list with the other collectibles of the same kind
            all_collects_1.append(collectible)

    pygame.display.flip()
