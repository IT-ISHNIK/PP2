import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
orange = (255,165,0)
purple = (238, 130, 238)
 
dis_width = 600
dis_height = 400
 
#food type
foods = [green, orange, red]
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
x = 0
foodisnothere = True
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 25)
horlines = []
verlines = []
for i in range(0, dis_width,10):
    verlines.append(i)
for i in range(0, dis_height,10):
    horlines.append(i)

 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(300,200))
    dis.blit(mesg, text_rect)
def score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
def drawlines(horlines, verlines):
    for x in verlines:
        pygame.draw.line(dis, white, (x, 0), (x, dis_height), 1)  # Corrected line
    for y in horlines:
        pygame.draw.line(dis, white, (0, y), (dis_width, y), 1)
def printlevel(level):
    value = score_font.render("Level: " + str(level), True, yellow)
    dis.blit(value, [490, 0])
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0

    x = 0
    foodisnothere = True

    RANDOM_COIN= pygame.USEREVENT + 1
    pygame.time.set_timer(RANDOM_COIN, 4000)
 
    snake_List = []
    Length_of_snake = 1
    level = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block ) / 10.0) * 10.0
    foody = round(random.randrange(40, dis_height - snake_block ) / 10.0) * 10.0
    randomfoodx = round(random.randrange(0, dis_width - snake_block ) / 10.0) * 10.0
    randomfoody = round(random.randrange(40, dis_height - snake_block ) / 10.0) * 10.0

    appear = False
    while not game_over:
        dis.fill(blue)
        drawlines(horlines, verlines)
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
 
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block 
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block 
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
            if event.type == RANDOM_COIN:
                randomfoodx = round(random.randrange(0, dis_width - snake_block ) / 10.0) * 10.0
                randomfoody = round(random.randrange(40, dis_height - snake_block ) / 10.0) * 10.0
                pygame.draw.rect(dis,purple, [randomfoodx, randomfoody, snake_block, snake_block])
                appear = True
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        level = ((Length_of_snake - 1) // 5) + 1
        speed_change = 3 * level
        if(appear):
            pygame.draw.rect(dis,purple, [randomfoodx, randomfoody, snake_block, snake_block])

        printlevel(level)
        if foodisnothere:
            x = random.randint(0, 2)
            foodisnothere = False
            color = foods[x]
        pygame.draw.rect(dis, color, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for i in snake_List[:-1]:
            if i == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        score(Length_of_snake - 1)

        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block ) / 10.0) * 10.0
            foody = round(random.randrange(40, dis_height - snake_block ) / 10.0) * 10.0
            if(x == 0):
                Length_of_snake += 1
            elif(x == 1):
                Length_of_snake += 2
            elif(x == 2):
                Length_of_snake += 3
            foodisnothere = True
        if x1 == randomfoodx and y1 == randomfoody:
            Length_of_snake +=1
            randomfoodx = -100
            randomfoody = -100
            appear = False
        clock.tick(snake_speed+speed_change)
 
    pygame.quit()
    quit()
 
 
gameLoop()