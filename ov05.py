import pygame
import random

# Инициализация PyGame
pygame.init()

# Настройки окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Игра на выживание")

# Загрузка изображений
player_image = pygame.image.load("img/player.png")  # Замените на путь к вашему изображению игрока
enemy_image = pygame.image.load("img/enemy.png")  # Замените на путь к вашему изображению врага
exit_image = pygame.image.load("img/exit.png")  # Замените на путь к вашему изображению выхода
yards_image = pygame.image.load("img/165.png")
yards_image = pygame.transform.scale(yards_image, (50, 50))

# Размеры и позиции
player_rect = player_image.get_rect()
enemy_rect = enemy_image.get_rect()
exit_rect = exit_image.get_rect()
yards_image_rect = yards_image.get_rect()

# Позиция игрока
player_rect.center = (400, 300)

# Позиция выхода
exit_rect.center = (400, 500)

# Сцены
class Scene:
    def __init__(self):
        self.running = True
        self.next_scene = None
        self.pressed_keys = set()  # Набор нажатых клавиш

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                    self.pressed_keys.add(event.key)
            elif event.type == pygame.KEYUP:
                if event.key in self.pressed_keys:
                    self.pressed_keys.remove(event.key)

    def update(self):
        # Перемещение игрока в зависимости от нажатых клавиш
        if pygame.K_LEFT in self.pressed_keys:
            self.player_rect.x -= 5
        if pygame.K_RIGHT in self.pressed_keys:
            self.player_rect.x += 5
        if pygame.K_UP in self.pressed_keys:
            self.player_rect.y -= 5
        if pygame.K_DOWN in self.pressed_keys:
            self.player_rect.y += 5

    def draw(self, screen):
        pass

class MainScene(Scene):
    def __init__(self):
        super().__init__()
        self.enemies = []
        self.spawn_enemies()
        self.player_rect = player_rect.copy()
        self.exit_rect = exit_rect.copy()

    def spawn_enemies(self):
        for _ in range(5):  # Количество врагов
            enemy_rect = enemy_image.get_rect()
            enemy_rect.center = (random.randint(100, 700), random.randint(100, 500))
            self.enemies.append(enemy_rect)

    def update(self):
        super().update()
        if self.player_rect.colliderect(self.exit_rect):
            self.running = False
            self.next_scene = SecondScene()

        # Проверка столкновения с врагами
        for enemy in self.enemies:
            if self.player_rect.colliderect(enemy):
                self.running = False
                self.next_scene = MainScene()  # Перезапуск уровня

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Черный фон
        screen.blit(player_image, self.player_rect)
        screen.blit(exit_image, self.exit_rect)
        for enemy in self.enemies:
            screen.blit(enemy_image, enemy)

class SecondScene(Scene):
    def __init__(self):
        super().__init__()
        self.player_rect = player_rect.copy()
        self.exit_rect = exit_rect.copy()
        self.yards = []
        self.add_yards()

    def add_yards(self):
        for _ in range(10):  # Количество врагов
            yards_rect = yards_image.get_rect()
            yards_rect.center = (random.randint(100, 700), random.randint(100, 500))
            self.yards.append(yards_rect)

    def update(self):
        super().update()
        if self.player_rect.colliderect(self.exit_rect):
            self.running = False
            self.next_scene = None

        # Проверка столкновения с врагами
        # Удаление дворов при столкновении с игроком
        self.yards = [y for y in self.yards if not self.player_rect.colliderect(y)]

    def draw(self, screen):
        screen.fill('white')  # Черный фон
        screen.blit(player_image, self.player_rect)
        screen.blit(exit_image, self.exit_rect)
        for y in self.yards:
            screen.blit(yards_image, y)

# Главный цикл
def main():
    clock = pygame.time.Clock()
    current_scene = MainScene()
    running = True
    while running:
        events = pygame.event.get()
        current_scene.handle_events(events)
        current_scene.update()

        if not current_scene.running:
            if current_scene.next_scene is None:
                running = False
            else:
                current_scene = current_scene.next_scene

        current_scene.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()