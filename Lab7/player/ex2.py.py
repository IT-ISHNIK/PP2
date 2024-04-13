import pygame
from pygame import mixer
import sys

pygame.init()
# mixer data
songs = ['A.D.D.S.U.V.mp3','Alright.mp3','song2.wav']
num_of_songs = 3
current_song = 1
paused = False

# font
text_font = pygame.font.SysFont("verdana" , 20)
m = text_font.render("Press m to play a song", True, ( 0, 0, 0))
k = text_font.render("Press k to pause", True, ( 0, 0, 0))
l = text_font.render("Press l to play next song", True, ( 0, 0, 0))
j = text_font.render("Press j to play previous song", True, ( 0, 0, 0))

#interface
width = 500
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music Player")


def play_song(current_song):
    global songs
    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play()

def is_paused(paused):
    if (paused):
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
def message():
    screen.blit(m, (0, 0))
    screen.blit(k, (0, 20))
    screen.blit(l, (0, 40))
    screen.blit(j, (0, 60))
def song(current_song):
    text = songs[current_song]
    textr = text_font.render(text, True, (0,0,0))
    textrect =textr.get_rect(center=(width/2, height/2))
    screen.blit(textr, textrect)



# Main loop
running = True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                play_song(current_song - 1)

            if event.key == pygame.K_l:
                current_song += 1
                current_song %= num_of_songs
                play_song(current_song - 1)

            if event.key == pygame.K_k:
                if(paused == True):
                    paused = False
                else:
                    paused = True
                is_paused(paused)

            if event.key == pygame.K_j:
                if(current_song == 1):
                    current_song = 1
                else:
                    current_song -= 1
                play_song(current_song - 1)

            if event.key == pygame.K_q:
                running = False
    message()
    song(current_song - 1)
    pygame.display.update()
pygame.quit()
sys.exit()
