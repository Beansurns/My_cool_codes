import pygame
import random
pygame.init()
surface = pygame.display.set_mode((1920,1028))
for y in range(60):
    for x in range(80):
        #r = random.randint(0,255)
        color = y*2.5,0,x*2.5
        pygame.draw.rect(surface, color, pygame.Rect(x*x//2.5, y*y//2.5, x, y))
        pygame.display.flip()

