import pygame

pygame.init()

#size
screen = pygame.display.set_mode((800, 600))
radius = 25
circleX  = 200
circleY = 200

#move
circleX_change = 0
circleY_change = 0


#text
pygame.display.set_caption("Task 3. Moving circle")
icon = pygame.image.load("ball.png")
pygame.display.set_icon(icon)

#running
running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                circleX_change = -0.5
            if event.key == pygame.K_RIGHT:
                circleX_change = 0.5
            if event.key == pygame.K_UP:
                circleY_change = -0.5
            if event.key == pygame.K_DOWN:
                circleY_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                circleX_change=0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                circleY_change=0
    circleX +=circleX_change
    if circleX > 750:
        circleX = 750
    if circleX < 50 :
        circleX = 50

    circleY +=circleY_change
    if circleY > 550:
        circleY = 550
    if circleY < 50:
        circleY = 50

    pygame.draw.rect(screen, (255,0,0), (circleX,circleY, 50, 50))
    pygame.display.update()
    
