import pygame 
import random

pygame.init()


# BASE SETTINGS
WIDTH, HEIGHT = 500,700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('RACE')
SPEED_START = 3
SPEED_DIFFERENCE = 1.5
LINE_CORDS = (130, 210, 290, 375)#(125, 180, 235, 290)
score = 0

# IMAGES
img_icon = pygame.image.load('lab9/race/images/1.png') # Logo

pygame.display.set_icon(img_icon)

img_road = pygame.image.load('lab9/race/images/road.png') # Background (Road)
img_player = pygame.image.load('lab9/race/images/player.png') # Player
img_coin = pygame.image.load('lab9/race/images/1.png') # Coin
img_enemy = pygame.image.load('lab9/race/images/enemycar.png')  # Enemy

# SOUNDS
sound_crash = pygame.mixer.Sound('lab9/race/sounds/crash.wav')
sound_crash.set_volume(0.1)

sound_coin = pygame.mixer.Sound('lab9/race/sounds/coin.mp3')
sound_coin.set_volume(0.05)

sound_bg = pygame.mixer.Sound('lab9/race/sounds/bg.mp3')
sound_bg.set_volume(0.1)

channel_coin = pygame.mixer.Channel(0)

# PLAYER CLASS
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = img_player
        self.rect = self.image.get_rect()
        self.bottom_pos = HEIGHT - 40
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = self.bottom_pos
        self.speed = SPEED_START 
        self.scoref = 0
        

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.move_ip(self.speed*0.7, 0)
        if keys[pygame.K_a]:
            self.rect.move_ip(-self.speed*0.7, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


        if score >= self.scoref + 20: 
            player.speed = min(player.speed + 0.2, 12)

            for enem in enemy_sprites: enem.speed = self.speed * SPEED_DIFFERENCE
            for coin in coin_sprites: coin.speed = self.speed
            road.speed = self.speed

            self.scoref = score

        # Up-Down
        # if keys[pygame.K_w]:
        #     self.rect.move_ip(0,-self.speed*0.7)
        # if keys[pygame.K_s]:
        #     self.rect.move_ip(0,self.speed*0.7)

        self.rect.clamp_ip(screen.get_rect())

# ENEMY CLASS
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemies):
        super().__init__()
        self.image = img_enemy
        self.rect = self.image.get_rect()
        self.speed = player.speed * SPEED_DIFFERENCE
        self.generate_random_rect(enemies)  


    def generate_random_rect(self, enemies):
        self.cordsX = LINE_CORDS

        while True:
            self.rect.centerx = random.choice(self.cordsX)
            self.rect.top = random.randint(-1200, -200)

            # check if the new enemy collides with any other enemy
            overlap = any(self.rect.colliderect(enemy.rect) for enemy in enemies if enemy != self)

            if not overlap:
                break  # exit the loop if there is no collision

    def move(self, enemies):
        if not game_over:
            self.rect.move_ip(0, self.speed)
            if self.rect.top > HEIGHT:
                self.generate_random_rect(enemies)

# COIN CLASS
class Coins(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = img_coin
        self.rect = self.image.get_rect()
        self.generate_random_rect()
        self.speed = player.speed
        
    def generate_random_rect(self):
        self.cordsX = LINE_CORDS
        self.rect.centerx = random.choice(self.cordsX)  #random.randint(20, WIDTH - self.rect.w)
        # self.rect.centerx = random.randint(0,2)
        self.rect.top = random.randint(-600, -250)
    
    def move(self):
        if not game_over:
            self.rect.move_ip(0, self.speed)
            if self.rect.top > HEIGHT:
                self.generate_random_rect()

# ROAD CLASS
class Road:
    def __init__(self):
        self.image = img_road
        self.y1 = 0
        self.y2 = -HEIGHT  # Second bg image is above the first one
        self.speed = player.speed  # Speed of moving = player speed

    def move(self):
        # Move the road down
        self.y1 += self.speed
        self.y2 += self.speed

        # If the first image completely disappeared — move it up
        if self.y1 >= HEIGHT:
            self.y1 = self.y2 - HEIGHT  # Move up
        # If the second image completely disappeared — move it up
        if self.y2 >= HEIGHT:
            self.y2 = self.y1 - HEIGHT  # Move up
    def draw(self, screen):
        # Draw two bg images
        screen.blit(self.image, (0, self.y1))
        screen.blit(self.image, (0, self.y2))


# Entities & Groups
player = Player()

enemy_sprites = pygame.sprite.Group()

enemy1 = Enemy(enemy_sprites)
enemy_sprites.add(enemy1)

enemy2 = Enemy(enemy_sprites)
enemy_sprites.add(enemy2)

enemy3 = Enemy(enemy_sprites)
enemy_sprites.add(enemy3)

coin1 = Coins()
coin2 = Coins()
coin3 = Coins()

road = Road()

all_sprites = pygame.sprite.Group(player, enemy1, enemy2, enemy3, coin1, coin2, coin3)
coin_sprites = pygame.sprite.Group(coin1, coin2, coin3)

# FPS
clock = pygame.time.Clock()
FPS = 120
# Flags
running = True
game_over = False  
was_crash = False

# Game Loop
while running:

    screen.blit(img_road, (0, 0))
    road.move() 
    road.draw(screen)

    if not game_over:

        # Background Music
        sound_crash.stop()
        sound_bg.play(-1)

        # Enabling sprites to move
        for entity in all_sprites:
            if isinstance(entity, Enemy):
                entity.move(enemy_sprites)
            else:
                entity.move()
            if entity.rect.top >= -100:
                screen.blit(entity.image, entity.rect)

        # Collision with enemy
        collided_enemy = pygame.sprite.spritecollideany(player, enemy_sprites)
        if collided_enemy:
            was_crash = True
            game_over = True

        # Collecting coins
        collided_coin = pygame.sprite.spritecollideany(player, coin_sprites)
        if collided_coin:
            channel_coin.play(sound_coin)
            collided_coin.generate_random_rect()
            score += 1

        # Disappearance of coins
        for enemy in enemy_sprites:
            collided_coin = pygame.sprite.spritecollideany(enemy, coin_sprites)
            if collided_coin:
                collided_coin.generate_random_rect()

        # Display Score
        font_score = pygame.font.Font("lab9/race/fonts/VT323-Regular.ttf", 36)
        text = font_score.render(f" Score: {score} ", True, (255, 255, 255), (240, 160, 55))
        font_score_rect = text.get_rect()
        screen.blit(text, (WIDTH - font_score_rect.w, 0))


    
    # Game Over Screen
    else:
        # Stop the background music
        sound_bg.stop()
        if was_crash:
            was_crash = False
            sound_crash.play(0)

        screen.fill("red")

        font_GO = pygame.font.Font("lab9/race/fonts/VT323-Regular.ttf", 50)
        text_gameOver = font_GO.render("Game Over!", True, (255, 255, 255))
        text_rect = text_gameOver.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_gameOver, text_rect)

        text_score = font_score.render(f"Score: {score}", True, (255, 255, 255))
        text_score_rect = text_score.get_rect(center=(WIDTH//2, HEIGHT//2 - 150))
        screen.blit(text_score, text_score_rect)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        

# UPDATE
    pygame.display.flip() # updates the screen
    clock.tick(FPS) # sets the FPS

pygame.quit()