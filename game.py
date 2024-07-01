import pygame
import random

# Инициализация Pygame
pygame.init()

# Определяем размеры окна и размеры клетки
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Класс змейки
class Snake:
    def __init__(self):
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = (0, -CELL_SIZE)
        self.grow = False

    # обновляет позицию змейки
    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = ((head_x + dir_x) % SCREEN_WIDTH, (head_y + dir_y) % SCREEN_HEIGHT)

        if new_head in self.positions:
            raise ValueError("Столкновение с самим собой!")

        self.positions = [new_head] + self.positions[:-1]

        if self.grow:
            self.positions.append(self.positions[-1])
            self.grow = False

    # изменяет направление змейки
    def change_direction(self, direction):
        opposite_direction = (-self.direction[0], -self.direction[1])
        if direction != opposite_direction:
            self.direction = direction

    # увеличивает длину змейки
    def grow_snake(self):
        self.grow = True

    # рисует змейку на экране
    def draw(self, screen):
        for position in self.positions:
            pygame.draw.rect(screen, GREEN, pygame.Rect(position[0], position[1], CELL_SIZE, CELL_SIZE))


# Класс еды
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    # задает случайную позицию еды
    def randomize_position(self):
        self.position = (random.randint(0, (SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

    # рисует еду на экране
    def draw(self, screen):
        pygame.draw.rect(screen, RED, pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))


# Класс игры
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Змейка")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    # главный цикл игры
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction((0, -CELL_SIZE))
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction((0, CELL_SIZE))
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction((-CELL_SIZE, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction((CELL_SIZE, 0))

            try:
                self.snake.move()
            except ValueError:
                print(f"Игра закончена! Ваши былы: {self.score}")
                running = False

            if self.snake.positions[0] == self.food.position:
                self.snake.grow_snake()
                self.food.randomize_position()
                self.score += 1

            self.screen.fill(BLACK)
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            pygame.display.update()

            self.clock.tick(10)

        pygame.quit()


# Запуск игры
if __name__ == "__main__":
    Game().run()