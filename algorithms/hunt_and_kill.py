import random

# Hunt-and-Kill 알고리즘을 사용한 미로 생성
# 이 알고리즘은 현재 위치에서 가능한 무작위 이동을 계속하다가 더 이상 이동할 수 없으면,
# 방문하지 않은 셀을 찾아 그곳으로 이동하여 과정을 반복합니다.
def generate_maze(width, height):
    grid = [[1 for _ in range(width)] for _ in range(height)]
    y, x = 1, 1
    grid[y][x] = 0

    while True:
        while True:
            directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
            random.shuffle(directions)
            moved = False
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 < ny < height-1 and 0 < nx < width-1 and grid[ny][nx] == 1:
                    grid[ny][nx] = grid[y+dy//2][x+dx//2] = 0
                    y, x = ny, nx
                    moved = True
                    break
            if not moved:
                break

        found = False
        for sy in range(1, height-1, 2):
            for sx in range(1, width-1, 2):
                if grid[sy][sx] == 1:
                    neighbors = [(0, 2), (2, 0), (0, -2), (-2, 0)]
                    random.shuffle(neighbors)
                    for dy, dx in neighbors:
                        ny, nx = sy + dy, sx + dx
                        if 0 < ny < height-1 and 0 < nx < width-1 and grid[ny][nx] == 0:
                            grid[sy][sx] = grid[sy+dy//2][sx+dx//2] = 0
                            y, x = sy, sx
                            found = True
                            break
                if found:
                    break
            if found:
                break
        if not found:
            break

    return grid
