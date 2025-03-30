import pygame
import math
import time

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("My_clock")

img = pygame.image.load("lab7/clock.png")
r_arm = pygame.image.load("lab7/rightarm.png")
l_arm = pygame.image.load("lab7/leftarm.png")
mainclock = pygame.transform.scale(img,(800,600))

clock = pygame.time.Clock()
# print(t_min)
# print(curr_time)

during = True
while during:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            during = 0
    
    curr_time = time.localtime()
    t_min = curr_time.tm_min
    t_sec = curr_time.tm_sec
    t_min_angl = 6 * t_min
    t_sec_angl = 6 * t_sec
    
    screen.blit(mainclock , (0,0))
    
                    
    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(r_arm, (800, 600)), -t_min_angl)
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2, 600 // 2 + 12))
    screen.blit(rotated_rightarm, rightarmrect)
    
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(l_arm, (40.95, 682.5)), -t_sec_angl)
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2, 600 // 2 + 10))
    screen.blit(rotated_leftarm, leftarmrect)
    
    pygame.display.flip() 
    clock.tick(90) #fps

pygame.quit()