import pygame
import os

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        pygame.mixer.music.load(r'C:\Users\Касымжомарт\Desktop\pp\lab7\music.mp3')
        pygame.mixer.music.play(0)
        
        pygame.display.flip()