import random

def generate_maze(width, height):
    def find(parent, i):
        if parent[i] != i:
            parent[i] = find(parent, parent[i])
        return parent[i]

    def union(parent, rank, x, y):
        xroot = find(parent, x)
        yroot = find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # 모든 셀을 벽으로 초기화
    grid = [[1 for _ in range(width)] for _ in range(height)]
    
    # 가능한 모든 벽(엣지)을 생성
    edges = []
    for y in range(1, height - 1, 2):
        for x in range(1, width - 1, 2):
            if x + 2 < width - 1:
                edges.append(((y, x), (y, x + 2)))
            if y + 2 < height - 1:
                edges.append(((y, x), (y + 2, x)))

    random.shuffle(edges)

    # 각 셀을 자신의 집합으로 초기화
    parent = {(y, x): (y, x) for y in range(1, height - 1, 2) for x in range(1, width - 1, 2)}
    rank = {(y, x): 0 for y in range(1, height - 1, 2) for x in range(1, width - 1, 2)}

    # 미로의 통로 생성
    for (y1, x1), (y2, x2) in edges:
        if find(parent, (y1, x1)) != find(parent, (y2, x2)):
            union(parent, rank, (y1, x1), (y2, x2))
            grid[y1][x1] = grid[y2][x2] = grid[(y1 + y2) // 2][(x1 + x2) // 2] = 0

    return grid