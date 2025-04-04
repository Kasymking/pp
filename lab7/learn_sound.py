import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

playlist = ["lab7/1.mp3", "lab7/2.mp3", "lab7/3.mp3"]
current_track = 0

def play_music():
    print(f"Playing: {playlist[current_track]}")
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

def stop_music():
    print("Music Stopped")
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Play Music")
                play_music()
            elif event.key == pygame.K_s:
                print("S Key Pressed - Stop Music")
                stop_music()
            elif event.key == pygame.K_RIGHT:
                print("Next Track")
                next_track()
            elif event.key == pygame.K_LEFT:
                print("Previous Track")
                prev_track()

    pygame.display.update()

pygame.quit()