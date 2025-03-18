import pygame
import os

pygame.init()
screen = pygame.display.set_mode((900, 600))
done = False
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((255, 255, 255))
        image = pygame.image.load("lab7/image.jpeg")  # Загружаем изображение
        screen.blit(image, (0, 0))  # Отображаем на экране
        
        pygame.display.flip()
        clock.tick(60)