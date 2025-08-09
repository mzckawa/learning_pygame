
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
player_y = height//3

# creating lists to store the collectibles 
list_collects_1_all = []
list_collects_1_lost = [] # to put the ones that reached the left side of the screen without being caught by the player
list_collects_1_earned = [] # to put the ones that collided with the player 

# creating the collectible's class
class Collectible:

    def __init__(self, x_pos, y_pos, widthcollec, heightcollec, speed):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = widthcollec
        self.height = heightcollec
        self.speed = speed
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.earned = False
        self.lost = False

    def draw_collec(self):
        pygame.draw.rect(screen, lilac, self.rect)

    def movement(self):
        self.x_pos -= self.speed

        if self.x_pos < - self.width:
            self.lost = True

        self.rect = pygame.Rect(self.x_pos, self.y_pos, 50, 50)

def creating_collect():
        
    list_collects_1_all.clear()
    list_collects_1_earned.clear()
    list_collects_1_lost.clear()

    # generating a new random number again
    amount_collect = randint(1, 10)

    # generating the objects of the class Collectibles with random positions
    for i in range (amount_collect):

    # generating random positions for the collectibles 
        x_collect = randint(player_x * 2, width) - 50
        y_collect = randint(height//2, height) - 50

        # creating the objects with the randomly-generated positions
        list_collects_1_all.append(Collectible(x_collect, y_collect))

    return amount_collect

amount_of_collect = creating_collect()
    
# naming some RGB tuples 
black = (0, 0, 0)
white = (255, 255, 255)
light_green = (128, 200, 128)
pink = (255, 0, 255)
lilac = (200, 162, 200)

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

    for i in range(amount_of_collect):

        # creating the collision conditional 
        if player.colliderect(list_collects_1_all[i]):
            list_collects_1_all[i].earned = True
            
        # keeping on drawing the object if it wasn't collected yet
        if list_collects_1_all[i] not in list_collects_1_earned:
            list_collects_1_all[i].draw_collec()
            list_collects_1_all[i].movement()

    pygame.display.flip()