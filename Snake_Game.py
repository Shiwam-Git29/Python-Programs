#PROJECT 2 :- Snake Game

import pygame
import random
import sys

# ------------------------------------------
# Simple Snake Game using pygame
# ------------------------------------------
# Controls   : Arrow keys (up/down/left/right)
# Objective  : Eat food to grow, avoid walls and yourself
# Features   : Scoreboard, restart prompt, smooth movement
# ------------------------------------------

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
# Size of each grid cell
CELL_SIZE = 20
# Derived grid dimensions
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

# Directions
UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)


def draw_grid(surface):
    """Optional grid lines for visual reference."""
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(surface, BLACK, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, BLACK, (0, y), (SCREEN_WIDTH, y))


def random_food_position(snake):
    """Return a random position not occupied by the snake."""
    positions = [(x, y) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)]
    available = list(set(positions) - set(snake))
    return random.choice(available)


def draw_snake(surface, snake_body):
    for segment in snake_body:
        rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, GREEN, rect)
        pygame.draw.rect(surface, BLACK, rect, 1)  # border


def draw_food(surface, position):
    rect = pygame.Rect(position[0] * CELL_SIZE, position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, RED, rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 36)

    def show_text(text, color, pos):
        img = font.render(text, True, color)
        screen.blit(img, pos)

    while True:  # game restart loop
        snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        direction = RIGHT
        food = random_food_position(snake)
        score = 0
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direction != DOWN:
                        direction = UP
                    elif event.key == pygame.K_DOWN and direction != UP:
                        direction = DOWN
                    elif event.key == pygame.K_LEFT and direction != RIGHT:
                        direction = LEFT
                    elif event.key == pygame.K_RIGHT and direction != LEFT:
                        direction = RIGHT

            # move snake
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])

            # check collisions with walls
            if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
                new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
                game_over = True
            # check self collision
            elif new_head in snake:
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == food:
                    score += 1
                    food = random_food_position(snake)
                else:
                    snake.pop()

            screen.fill(WHITE)
            # draw_grid(screen)  # uncomment to show grid lines
            draw_snake(screen, snake)
            draw_food(screen, food)
            show_text(f"Score: {score}", BLUE, (10, 10))

            pygame.display.flip()
            clock.tick(10)  # 10 frames per second

        # game over screen
        screen.fill(WHITE)
        show_text("Game Over", RED, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 40))
        show_text(f"Final Score: {score}", BLUE, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        show_text("Press R to play again or Q to quit", BLACK, (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2 + 40))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()


if __name__ == "__main__":
    main()
