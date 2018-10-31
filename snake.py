import pygame
import sys
import random


class SnakeBodyElement:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        return pygame.Rect(self.x, self.y, 10, 10)


pygame.init()
max_tps = 12.5
step: int = 10
s = pygame.display.set_mode((480, 360))
clock = pygame.time.Clock()
delta = 0.0
random.seed()

x = random.randrange(100, 380, 10)
y = random.randrange(60, 300, 10)
direction = 2
snake = [
    SnakeBodyElement(x, y),
    SnakeBodyElement(x+10, y),
    SnakeBodyElement(x+20, y)
]

fruit = [random.randrange(100, 380, 10), random.randrange(60, 300, 10)]


def eat(snake_m):
    x = snake_m[0].x
    y = snake_m[0].y
    if direction == 0:
        x += step
    elif direction == 1:
        y += step
    elif direction == 2:
        x -= step
    elif direction == 3:
        y -= step
    new_body_element = SnakeBodyElement(x, y)
    for el in snake_m:

        if new_body_element.x == el.x and new_body_element.y == el.y:
            print("snake eat her self")
            sys.exit(0)
    snake_m.insert(0, new_body_element)


def move(snake_m):
    eat(snake_m)
    snake_m.pop()


while True:
    # events
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit(0)

    # ticks
    delta += clock.tick()/1000.0
    while delta > 1 / max_tps:
        delta -= 1 / max_tps

        # inputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and direction != 0:
            direction = 2
        if keys[pygame.K_RIGHT] and direction != 2:
            direction = 0
        if keys[pygame.K_DOWN] and direction != 3:
            direction = 1
        if keys[pygame.K_UP] and direction != 1:
            direction = 3
        if keys[pygame.K_SPACE]:
            eat(snake)

        # moving
        move(snake)

        # condition of lose
        if snake[0].x < 0 or snake[0].x > 480 or snake[0].y < 0 or snake[0].y > 360:
            print("snake move out of board")
            sys.exit(0)

        # condition if eat
        if snake[0].x == fruit[0] and snake[0].y == fruit[1]:
            eat(snake)
            fruit = [random.randrange(100, 380, 10), random.randrange(60, 300, 10)]

        # draw
        s.fill((255, 255, 255))
        for bodyEl in snake:
            pygame.draw.rect(s, (0, 128, 128), bodyEl.draw())
        pygame.draw.rect(s, (255, 0, 0), pygame.Rect(fruit[0], fruit[1], 10, 10))
        pygame.display.flip()
