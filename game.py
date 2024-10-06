import pygame
from maze import Maze
from maze_validator import validate_and_regenerate_maze
from player import Player

class Game:
    def __init__(self, maze_width, maze_height, cell_size, algorithm='dfs', seed=None):
        pygame.init()
        self.cell_size = cell_size
        self.screen_width = maze_width * cell_size
        self.screen_height = maze_height * cell_size
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("미로 게임")

        # Maze 클래스 초기화 시 검증 로직 추가
        self.maze = Maze(maze_width, maze_height, algorithm, seed)
        self.maze.grid = validate_and_regenerate_maze(
            lambda w, h: self.maze.generate_maze(self.maze.algorithm),
            maze_width, maze_height
        )

        start_x, start_y = self.maze.get_entrance()
        self.player = Player(start_x + 0.5, start_y + 0.5, cell_size)  # 셀의 중앙에 위치하도록 0.5를 더합니다
        self.clock = pygame.time.Clock()

    def draw_maze(self):
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                if self.maze.is_wall(x, y):
                    pygame.draw.rect(self.screen, (0, 0, 0),
                                     (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, (200, 200, 200),
                                     (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

        exit_x, exit_y = self.maze.get_exit()
        pygame.draw.rect(self.screen, (0, 255, 0),
                         (exit_x * self.cell_size, exit_y * self.cell_size, self.cell_size, self.cell_size))

    def check_win(self):
        exit_x, exit_y = self.maze.get_exit()
        return int(self.player.x) == exit_x and int(self.player.y) == exit_y

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
            dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]

            if dx != 0 or dy != 0:
                print(f"Input: dx={dx}, dy={dy}")  # 디버그 출력
                self.player.move(dx, dy, self.maze)

            self.screen.fill((255, 255, 255))
            self.draw_maze()
            self.player.draw(self.screen)
            pygame.display.flip()

            if self.check_win():
                print("축하합니다! 미로를 탈출했습니다!")
                running = False

            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    available_algorithms = Maze.get_available_algorithms()
    print("사용 가능한 미로 생성 알고리즘:")
    for i, algo in enumerate(available_algorithms, 1):
        print(f"{i}. {algo}")
    
    choice = int(input("사용할 알고리즘 번호를 선택하세요: ")) - 1
    selected_algorithm = available_algorithms[choice]
    
    seed = int(input("랜덤 시드를 입력하세요 (무작위로 하려면 0 입력): ") or 0)
    seed = seed if seed != 0 else None
    
    game = Game(33, 33, 20, algorithm=selected_algorithm, seed=seed)
    game.run()
