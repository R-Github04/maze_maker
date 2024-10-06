import random

# 재귀적 분할 알고리즘을 사용한 미로 생성
# 이 알고리즘은 큰 공간을 재귀적으로 더 작은 공간으로 분할하여 미로를 만듭니다.
# 각 분할 단계에서 벽을 세우고 무작위로 통로를 만들어 미로의 구조를 형성합니다.
def generate_maze(width, height):
    def divide(x, y, w, h, orientation):
        if w < 2 or h < 2:
            return

        horizontal = orientation if orientation is not None else random.choice([True, False])

        wx = x + (0 if horizontal else random.randint(0, w-2))
        wy = y + (random.randint(0, h-2) if horizontal else 0)

        px = wx + (0 if horizontal else 1)
        py = wy + (1 if horizontal else 0)

        dx = 1 if horizontal else 0
        dy = 0 if horizontal else 1

        length = w if horizontal else h
        
        # 벽에 최소 2개의 통로를 만듭니다.
        passages = random.sample(range(length), min(2, length))

        for i in range(length):
            if i in passages or wx == px or wy == py:
                grid[wy][wx] = 0
            else:
                grid[wy][wx] = 1
            wx += dx
            wy += dy

        nx, ny = x, y
        nw, nh = (w, wy-y+1) if horizontal else (wx-x+1, h)
        divide(nx, ny, nw, nh, horizontal)

        nx, ny = (x, wy+1) if horizontal else (wx+1, y)
        nw, nh = (w, y+h-wy-1) if horizontal else (x+w-wx-1, h)
        divide(nx, ny, nw, nh, horizontal)

    grid = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(width):
        grid[0][i] = grid[height-1][i] = 1
    for i in range(height):
        grid[i][0] = grid[i][width-1] = 1
    
    divide(1, 1, width-2, height-2, None)
    return grid