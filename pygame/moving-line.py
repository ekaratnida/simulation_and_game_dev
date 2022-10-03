#! /usr/bin/env python

import pygame
import random
y = 0
dir = 1
running = 1
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
linecolor = 255, 0, 0
bgcolor = 255, 255, 255

w = [random.randint(100,width-100) for r in range(5) ]
h = [random.randint(100,height-100) for r in range(5) ]
z = zip(w,h)
print(w," ",h)
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    screen.fill(bgcolor)
    #pygame.draw.line(screen, linecolor, (0, y), (width-1, y))
    
    #for w,h in z:
    #print(w,",",h)
    for i,j in zip(w,h):
        print(i," ",j)
        pygame.draw.circle(screen,linecolor, (i, j), 10, 0)
    

    #y += dir
    #if y == 0 or y == height-1: dir *= -1

    pygame.display.flip()
    #pygame.time.delay(1)