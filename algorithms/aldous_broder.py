import random

# Aldous-Broder 알고리즘을 사용한 미로 생성
# 이 알고리즘은 무작위 걸음을 사용하여 모든 셀을 방문할 때까지 이동합니다.
# 처음 방문하는 셀로 이동할 때마다 통로를 만들어 미로를 형성합니다.
def generate_maze(width, height):
    grid = [[1 for _ in range(width)] for _ in range(height)]
    y, x = 1, 1
    grid[y][x] = 0
    unvisited = (width // 2) * (height // 2) - 1

    while unvisited > 0:
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        dy, dx = random.choice(directions)
        ny, nx = y + dy, x + dx

        if 0 < ny < height-1 and 0 < nx < width-1:
            if grid[ny][nx] == 1:
                grid[ny][nx] = grid[y+dy//2][x+dx//2] = 0
                unvisited -= 1
            y, x = ny, nx

    return grid
