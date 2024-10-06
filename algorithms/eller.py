import random

# Eller의 알고리즘을 사용한 미로 생성
# 이 알고리즘은 미로를 한 줄씩 생성합니다.
# 각 셀을 집합으로 관리하며, 인접한 셀들을 무작위로 연결하거나 분리하여 미로를 만듭니다.
def generate_maze(width, height):
    def get_set(x, row):
        if x not in row:
            row[x] = next_set[0]
            next_set[0] += 1
        return row[x]

    grid = [[1 for _ in range(width)] for _ in range(height)]
    next_set = [1]
    row = {}

    for y in range(1, height-1, 2):
        for x in range(1, width-1, 2):
            set_id = get_set(x, row)
            grid[y][x] = 0

            if x+2 < width-1 and (random.random() < 0.5 or y == height-2):
                if get_set(x+2, row) != set_id:
                    grid[y][x+1] = 0
                    row[x+2] = set_id

        if y+2 < height-1:
            next_row = {}
            for x in range(1, width-1, 2):
                if random.random() < 0.5:
                    next_row[x] = row[x]
                    grid[y+1][x] = 0

            row = next_row

    return grid
