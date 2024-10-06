import pygame
import math

class Player:
    def __init__(self, x, y, cell_size):
        self.x = float(x)
        self.y = float(y)
        self.cell_size = cell_size
        self.move_speed = 0.1  # 이동 속도를 조정합니다.

    def move(self, dx, dy, maze):
        new_x = self.x + dx * self.move_speed
        new_y = self.y + dy * self.move_speed

        # 충돌 검사
        if not maze.is_wall(int(new_x), int(new_y)):
            self.x = new_x
            self.y = new_y
            print(f"Player moved to: ({self.x}, {self.y})")  # 디버그 출력
        else:
            print(f"Collision detected at: ({new_x}, {new_y})")  # 디버그 출력

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0),
                           (int(self.x * self.cell_size),
                            int(self.y * self.cell_size)),
                           int(self.cell_size * 0.4))
