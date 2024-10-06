import random

def generate_maze(width, height):
    grid = [[1 for _ in range(width)] for _ in range(height)]
    
    def dfs(x, y):
        grid[y][x] = 0
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < width - 1 and 0 < ny < height - 1 and grid[ny][nx] == 1:
                grid[y + dy // 2][x + dx // 2] = 0
                dfs(nx, ny)

    dfs(1, 1)
    return grid
