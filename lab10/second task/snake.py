import pygame
import random
import db

# Init user and show previous high level
db.input_user()
highest = db.show_highest_level()
if highest and highest[0][0]:
    print(f"Your highest level: {highest[0][0]}")
else:
    print("Welcome! No records found yet.")
    db.add_user(db.current_user)

pygame.init()
pygame.mixer.init()

# settings
WIDTH = 600
HEIGHT = 600
CELL = 30
FPS_START = 6

# Sounds
sound_eating = pygame.mixer.Sound('lab10/second task/music_food.mp3')
sound_eating.set_volume(0.2)
channel_eating = pygame.mixer.Channel(0)

screen = pygame.display.set_mode((HEIGHT, WIDTH))
game_over = False

# Colors
colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

# Draw chessboard grid
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# coordinates
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Snake class
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 0, -1

    def move(self):
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
        if new_head.x < 0 or new_head.x >= WIDTH // CELL or new_head.y < 0 or new_head.y >= HEIGHT // CELL:
            return True
        if new_head in self.body:
            return True
        self.body.insert(0, new_head)
        self.body.pop()
        return False

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        global score, FPS, lvl, level_threshold
        if self.body[0] == food.pos:
            self.body.append(Point(self.body[-1].x, self.body[-1].y))
            food.move(self)
            score += food.cost
            channel_eating.play(sound_eating)
            if score >= level_threshold:
                FPS += 0.5
                lvl += 1
                level_threshold += 5

# Food class
class Food:
    def __init__(self):
        self.last_spawn_time = pygame.time.get_ticks()
        self.move(snake=None)

    def move(self, snake):
        while True:
            self.x = random.randrange(0, WIDTH // CELL)
            self.y = random.randrange(0, HEIGHT // CELL)
            self.pos = Point(self.x, self.y)
            self.cost = random.randrange(1, 4)
            if snake is None or self.pos not in snake.body:
                self.last_spawn_time = pygame.time.get_ticks()
                break

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

# Game settings
FPS = FPS_START
score = 0
lvl = 1
level_threshold = 10
clock = pygame.time.Clock()
snake = Snake()
food = Food()
running = True

while running:
    if not game_over:
        if pygame.time.get_ticks() - food.last_spawn_time > 10000:
            food.move(snake)

        draw_grid_chess()
        game_over = snake.move()
        snake.check_collision(food)
        snake.draw()
        food.draw()

        font_score = pygame.font.Font(None, 36)
        text = font_score.render(f" Score: {score} ", True, colorBLACK)
        screen.blit(text, (WIDTH - 150, 10))

        font_speed = pygame.font.Font(None, 36)
        text_speed = font_speed.render(f" Level: {lvl} ", True, colorBLACK)
        screen.blit(text_speed, (10, 10))

    else:
        screen.fill('red')
        font_GO = pygame.font.Font(None, 50)
        text_gameOver = font_GO.render("Game Over!", True, colorWHITE)
        screen.blit(text_gameOver, text_gameOver.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

        font_restart = pygame.font.Font(None, 25)
        text_restart = font_restart.render('Press "Space" to Restart', True, colorWHITE)
        screen.blit(text_restart, text_restart.get_rect(center=(WIDTH // 2, HEIGHT - 40)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:
                db.add_or_update_score(score,lvl)  # Сохраняем результат
                FPS = FPS_START
                score = 0
                lvl = 1
                level_threshold = 10
                game_over = False
                snake = Snake()
                food = Food()
                snake.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
                snake.dx, snake.dy = 0, -1

        elif event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_ESCAPE:
                print("Game exited.")
                running = False

            elif event.key == pygame.K_p:
                print("Game paused. Press 'C' to resume.") # Stopping the program
                paused = True
                db.add_or_update_score(score,lvl)

                while paused:
                    for pause_event in pygame.event.get():
                        if pause_event.type == pygame.QUIT:
                            paused = False
                            running = False
                        elif pause_event.type == pygame.KEYDOWN:
                            if pause_event.key == pygame.K_c:
                                paused = False
                    screen.fill(colorWHITE)
                    font_pause = pygame.font.Font(None, 50)
                    pause_text = font_pause.render("PAUSED", True, colorBLACK)
                    screen.blit(pause_text, pause_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
                    pygame.display.flip()
                    clock.tick(5)

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                snake.dx = 0
                snake.dy = -1

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
db.connection.close()
