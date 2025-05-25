print("Name: Kushagra Suri")
print("USN: 1AY24AI058")
print("Section: M")
import os
import random
def create_grid(size):
    return [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]
def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(' '.join(['█' if cell else ' ' for cell in row]))
def count_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            count += grid[nx][ny]
    return count
def update_grid(grid):
    new_grid = [[0] * len(grid) for _ in range(len(grid))]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == 1 and neighbors in (2, 3):
                new_grid[x][y] = 1
            elif grid[x][y] == 0 and neighbors == 3:
                new_grid[x][y] = 1
    return new_grid
def main(size, iterations):
    grid = create_grid(size)
    for _ in range(iterations):
        print_grid(grid)
        grid = update_grid(grid)
        input("Press Enter to continue...")
if __name__ == "__main__":
    main(size=10, iterations=10)
