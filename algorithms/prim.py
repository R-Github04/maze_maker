import random

def generate_maze(width, height):
    grid = [[1 for _ in range(width)] for _ in range(height)]
    start_y, start_x = 1, 1
    grid[start_y][start_x] = 0
    walls = [(start_y, start_x - 1), (start_y, start_x + 1),
            (start_y - 1, start_x), (start_y + 1, start_x)]
    
    while walls:
        wall_y, wall_x = random.choice(walls)
        walls.remove((wall_y, wall_x))
        
        if 0 < wall_x < width - 1 and 0 < wall_y < height - 1:
            cell_count = sum(1 for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]
                             if 0 < wall_y + dy < height - 1 and 0 < wall_x + dx < width - 1 and grid[wall_y + dy][wall_x + dx] == 0)
            
            if cell_count == 1:
                grid[wall_y][wall_x] = 0
                for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    ny, nx = wall_y + dy, wall_x + dx
                    if 0 < ny < height - 1 and 0 < nx < width - 1 and grid[ny][nx] == 1:
                        walls.append((ny, nx))
    
    return grid
