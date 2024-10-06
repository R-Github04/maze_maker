import random

# Wilson의 알고리즘을 사용한 미로 생성
# 이 알고리즘은 무작위 걸음(random walk)을 사용하여 미로를 생성합니다.
# 루프가 제거된 경로를 통해 모든 셀을 연결하여 완벽한 미로를 만듭니다.
def generate_maze(width, height):
    grid = [[1 for _ in range(width)] for _ in range(height)]
    cells = [(y, x) for y in range(1, height-1, 2) for x in range(1, width-1, 2)]
    
    # 시작점을 무작위로 선택
    start = random.choice(cells)
    cells.remove(start)
    grid[start[0]][start[1]] = 0

    while cells:
        cell = random.choice(cells)
        path = [cell]
        
        while cell in cells:
            directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
            dy, dx = random.choice(directions)
            next_cell = (cell[0] + dy, cell[1] + dx)
            
            if 0 < next_cell[0] < height-1 and 0 < next_cell[1] < width-1:
                path.append(next_cell)
                if next_cell not in cells:
                    for c, n in zip(path[:-1], path[1:]):
                        grid[c[0]][c[1]] = 0
                        grid[(c[0] + n[0]) // 2][(c[1] + n[1]) // 2] = 0
                        if c in cells:
                            cells.remove(c)
                    break
                cell = next_cell

    return grid