def is_valid_maze(grid):
    """
    미로의 유효성을 검사합니다.
    1. 모든 빈 칸이 연결되어 있는지 확인
    2. 시작점에서 끝점까지 경로가 존재하는지 확인
    """
    height, width = len(grid), len(grid[0])
    start = (1, 0)  # 입구 위치
    end = (height - 2, width - 1)  # 출구 위치
    
    # DFS를 사용하여 모든 빈 칸이 연결되어 있는지 확인
    visited = [[False for _ in range(width)] for _ in range(height)]
    stack = [start]
    visited[start[0]][start[1]] = True
    
    while stack:
        y, x = stack.pop()
        if (y, x) == end:
            return True  # 끝점에 도달할 수 있음
        
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < height and 0 <= nx < width and grid[ny][nx] == 0 and not visited[ny][nx]:
                stack.append((ny, nx))
                visited[ny][nx] = True
    
    return False  # 끝점에 도달할 수 없음

def preserve_entrance_exit(grid):
    """
    미로의 입구와 출구를 보존합니다.
    """
    height, width = len(grid), len(grid[0])
    grid[1][0] = 0  # 입구
    grid[1][1] = 0  # 입구 옆 칸
    grid[height - 2][width - 1] = 0  # 출구
    grid[height - 2][width - 2] = 0  # 출구 옆 칸
    return grid

def validate_and_regenerate_maze(generate_maze_func, width, height, max_attempts=10):
    """
    유효한 미로를 생성할 때까지 미로 생성을 반복합니다.
    입구와 출구를 보존합니다.
    """
    for _ in range(max_attempts):
        grid = generate_maze_func(width, height)
        grid = preserve_entrance_exit(grid)  # 입구와 출구 보존
        if is_valid_maze(grid):
            return grid
    
    raise Exception("유효한 미로를 생성할 수 없습니다.")