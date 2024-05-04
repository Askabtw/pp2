import pygame
import datetime
import os

pygame.init()
pygame.mixer.init()

HEIGHT, WIDHT = 500, 500
screen = pygame.display.set_mode(size = (HEIGHT, WIDHT))
clock = pygame.time.Clock()
pygame.display.set_caption('player')

keys=pygame.key.get_pressed()
musicplay = False
fname = r"C:\Users\Elzhan\pp2\pp2-22B030522\tsis7\music"
i =0
musiclist = os.listdir(fname)
musictype = fname + "\\"+ musiclist[i]
def chosemusic(a, musiclist, i): 
    if a == 2:
        if i == 0:
            i = len(musiclist)-1
        else:
            i = i-1  
    if a == 1:
        if i == len(musiclist)-1:
            i = 0
        else:
            i += 1
    return fname + "\\"+ musiclist[i]


a =0
running = True
while running:
    screen.fill((155, 155, 155))
    a += 1
    if a == 1:
        pygame.mixer.music.load('music//'+musiclist[i])
        pygame.mixer.music.play()
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pygame.mixer.music.stop()
                if i -1 == -1:
                    i = len(musiclist)
                i -= 1
                musicplay = True
                pygame.mixer.music.load('music//'+musiclist[i])
                pygame.mixer.music.play()
            if event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                if i+1 == len(musiclist):
                    i = -1
                i += 1
                pygame.mixer.music.load('music//'+musiclist[i])
                pygame.mixer.music.play()
                
            if event.key == pygame.K_SPACE:
                musicplay = not musicplay
                if musicplay == True:
                    pygame.mixer.music.pause()
                if musicplay == False:
                    pygame.mixer.music.unpause()
            



    pygame.display.flip()

    clock.tick(60)