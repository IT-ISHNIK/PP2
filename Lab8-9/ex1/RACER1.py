import pygame
import random
import time
import math
pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

WIDTH , HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT ))
screen.fill((255,255,255))


pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("racing.png")
pygame.display.set_icon(icon)

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCORE = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 50)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("bg.jpg")

#enemy
enemyX = random.randint(0,WIDTH-64)
enemyY = 0
enemyY_change = 5
#player
playerX = 200
playerY = 520
playerX_change = 0
playerImg = pygame.image.load("player.png")
enemyImg = pygame.image.load("enemy.png")
#Coin
coinX = random.randint(0, WIDTH- 64)
coinY = 0
coinscore = 0
cointype = ["star.png", "money-bag.png", "treasure.png"]
x = 0 # order of type in array


#player
def player(x,y):
    screen.blit(playerImg, (x,y))

#enemy
def enemy(x,y):
    screen.blit(enemyImg, (x,y))

#collision
def iscollision(enemyX,enemyY,playerX, playerY):
    distance = math.sqrt(math.pow(enemyX - playerX, 2) + math.pow(enemyY - playerY, 2))
    if distance < 27:
        return True
    else:
        return False
#text
def game_over_text():
    over_text = font.render("Game Over", True, BLACK)
    text_rect = over_text.get_rect(center=(200, 300))
    screen.blit(over_text, text_rect)
#score
def show_score(x,y):
    score = font_small.render("Score :" + str(SCORE), True, (255,255,255))
    screen.blit(score, (x,y))
#coin blit
def coinblit(coinX, coinY, cointype, x):
    global coinscore
    if x == 0:
        coinscore = 1
    elif x == 1:
        coinscore = 3
    elif x == 2:
        coinscore = 5
    coinimage = pygame.image.load(cointype[x])
    screen.blit(coinimage,(coinX,coinY))
#COIN collision
def coin_collision(coinX,  coinY, playerX, playerY):
    distance = math.sqrt(math.pow(coinX - playerX, 2) + math.pow(coinY - playerY, 2))
    if distance < 27:
        return True
    else:
        return False

#Adding a new User event 
# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)
SPAWN_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_COIN, 2000)
running = True
while running:
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        # if event.type == INC_SPEED:
        #     enemyY_change+=1
        if event.type == SPAWN_COIN:
            coinX = random.randint(0, WIDTH- 64)
            coinY = 0
            x = random.randint(0, 2)
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYUP: # KEYUP - event happens when keyboard pressing is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    change = (SCORE // 5) * 2
    enemyY_change = 5 + change
    playerX += playerX_change
    if playerX <=0: 
        playerX = 0
    elif playerX >= WIDTH - 64:
        playerX = WIDTH - 64

    enemyY+=enemyY_change
    coinY+=enemyY_change
    if(enemyY >= HEIGHT):
        enemyX = random.randint(0, WIDTH - 64)
        enemyY = 0
    collision = iscollision(enemyX, enemyY,playerX,playerY)

    if collision:
        pygame.mixer.Sound('explosion.wav').play()
        time.sleep(1)
        game_over_text()
        pygame.display.update()
        time.sleep(1)
        pygame.quit()
    check = coin_collision(coinX,  coinY, playerX, playerY)
    if check:
        coinX = -100
        SCORE+= coinscore
    player(playerX, playerY)
    coinblit(coinX,coinY, cointype, x)
    enemy(enemyX,enemyY) 
    show_score(10,10)


    # Check for collisions with coins
    pygame.display.update()
    FramePerSec.tick(FPS)
