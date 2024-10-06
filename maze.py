import random
import importlib
import os

class Maze:
    def __init__(self, width, height, algorithm='dfs', seed=None):
        # 미로의 최소 크기를 33x33으로 설정하고, 홀수로 만듭니다.
        self.width = max(width // 2 * 2 + 1, 33)
        self.height = max(height // 2 * 2 + 1, 33)
        
        self.algorithm = algorithm
        
        self.seed = seed
        if self.seed:
            random.seed(self.seed)
        
        self.entrance = (0, 1)  # 입구 위치를 명시적으로 정의
        self.exit = (width - 1, height - 2)  # 출구 위치를 명시적으로 정의
        
        self.grid = self.generate_maze(algorithm)
        self.add_outer_walls()
        self.create_entrance_exit()

    def generate_maze(self, algorithm):
        # 알고리즘 모듈을 동적으로 불러옵니다.
        try:
            module = importlib.import_module(f'algorithms.{algorithm}')
            generate_function = getattr(module, 'generate_maze')
            grid = generate_function(self.width, self.height)
            if grid is None or not isinstance(grid, list) or len(grid) != self.height:
                raise ValueError(f"알고리즘 {algorithm}이 유효한 미로 그리드를 반환하지 않았습니다.")
            return grid
        except ImportError:
            raise ValueError(f"알 수 없는 알고리즘입니다: {algorithm}")
        except AttributeError:
            raise ValueError(f"알고리즘 모듈 {algorithm}에 generate_maze 함수가 없습니다.")
        except Exception as e:
            raise ValueError(f"미로 생성 중 오류 발생: {str(e)}")

    def add_outer_walls(self):
        # 미로 외곽에 벽을 추가합니다.
        for y in range(self.height):
            self.grid[y][0] = self.grid[y][self.width - 1] = 1
        for x in range(self.width):
            self.grid[0][x] = self.grid[self.height - 1][x] = 1

    def create_entrance_exit(self):
        # 입구와 출구를 생성하고 주변 공간을 확보합니다.
        entrance_x, entrance_y = self.entrance
        exit_x, exit_y = self.exit
        self.grid[entrance_y][entrance_x] = 0
        self.grid[entrance_y][entrance_x + 1] = 0  # 입구 바로 옆 칸도 비움
        self.grid[exit_y][exit_x] = 0
        self.grid[exit_y][exit_x - 1] = 0  # 출구 바로 옆 칸도 비움

    def is_wall(self, x, y):
        # 주어진 좌표가 벽인지 확인합니다.
        int_x, int_y = int(x), int(y)
        if 0 <= int_x < self.width and 0 <= int_y < self.height:
            return self.grid[int_y][int_x] == 1
        return True  # 미로 밖의 영역은 벽으로 처리합니다.

    def get_entrance(self):
        return self.entrance

    def get_exit(self):
        return self.exit

    @staticmethod
    def get_available_algorithms():
        # algorithms 폴더에서 사용 가능한 알고리즘 목록을 반환합니다.
        algorithm_dir = os.path.join(os.path.dirname(__file__), 'algorithms')
        algorithms = [f[:-3] for f in os.listdir(algorithm_dir) 
                      if f.endswith('.py') and f != '__init__.py']
        return algorithms
