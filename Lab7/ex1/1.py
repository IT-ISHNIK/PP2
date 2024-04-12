import pygame
import datetime

pygame.init()
clock = pygame.time.Clock()

left_arm = pygame.image.load('leftarm.png')
right_arm = pygame.image.load('rightarm1.png')
clock_image = pygame.image.load('mainclock.png')

w, h = clock_image.get_size()
screen = pygame.display.set_mode((w, h))

angle = 360
rangle = 360

done = False

while not done:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pos = (screen.get_width() / 2, screen.get_height() / 2)
    screen.fill(0)

    # Time now
    now = datetime.datetime.now()


    # Angle for seconds
    seconds = now.second
    seconds_angle = 360 * seconds / 60


    # angle for minuts
    minutes = now.minute
    minutes_angle = 360 * minutes / 60 + seconds_angle / 60

   
    # rotation for seconds
    rotated_left_arm = pygame.transform.rotate(left_arm, -seconds_angle)
    rotated_left_arm_rect = rotated_left_arm.get_rect(center=pos)

    # rotations for minuts
    rotated_right_arm = pygame.transform.rotate(right_arm, -minutes_angle)
    rotated_right_arm_rect = rotated_right_arm.get_rect(center=pos)

    # blit
    screen.blit(clock_image, (0,0))
    screen.blit(rotated_left_arm, rotated_left_arm_rect)
    screen.blit(rotated_right_arm, rotated_right_arm_rect)
 


    pygame.display.flip()

pygame.quit()