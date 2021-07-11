import pygame as pg
import random
import time

def Main():
    # Variables
    sq1pos = [25, 100]
    sq2pos = [25, 200]
    sq3pos = [25, 300]
    sq4pos = [25, 400]
    var = 0

    # Initializing pygame
    pg.init()

    # Music
    WHITE = (128, 128, 128)

    # Creating the window
    screen = pg.display.set_mode((1280,550))
    pg.mixer.music.load('sound/bmusic.wav')
    pg.mixer.music.play(-1)

    # Other variables
    WHITE = (128, 128, 128)
    backround = pg.image.load('textures/asphalt.jpeg')
    car01 = pg.image.load('textures/car01.png')
    car02 = pg.image.load('textures/car02.png')
    car03 = pg.image.load('textures/car03.png')
    car04 = pg.image.load('textures/car04.png')

    # Game loop
    running = True
    while running:
        screen.blit(backround, (0,0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        pg.draw.rect(screen, WHITE, (1200,0,25,550))
        screen.blit(car03, sq3pos)
        screen.blit(car04, sq4pos)
        screen.blit(car01, sq1pos)
        screen.blit(car02, sq2pos)

        pg.display.update()

        if var == 0:
            time.sleep(3)
            var = 1

        sq1pos[0] += random.uniform(0.1, 1.5)
        sq2pos[0] += random.uniform(0.1, 1.5)
        sq3pos[0] += random.uniform(0.1, 1.5)
        sq4pos[0] += random.uniform(0.1, 1.5)

Main()
