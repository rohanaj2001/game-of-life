import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
FPS = 10

# Colors
DEAD_COLOR = (0, 0, 0)
ALIVE_COLOR = (255, 255, 255)

def create_grid():
    return np.random.choice([0, 1], size=(GRID_WIDTH, GRID_HEIGHT))

def update_grid(grid):
    new_grid = grid.copy()

    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            neighbors = np.sum(grid[i - 1:i + 2, j - 1:j + 2]) - grid[i, j]
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1

    return new_grid

def draw_grid(screen, grid):
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            color = ALIVE_COLOR if grid[i, j] == 1 else DEAD_COLOR
            pygame.draw.rect(screen, color, (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()

    grid = create_grid()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grid = update_grid(grid)

        screen.fill(DEAD_COLOR)
        draw_grid(screen, grid)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
