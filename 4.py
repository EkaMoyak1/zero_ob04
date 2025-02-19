import pygame
import random
import sys

# Инициализация PyGame
pygame.init()

# Настройки окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Игра на выживание")

# Загрузка изображений
player_image = pygame.image.load("img/player.png")  # Замените на путь к вашему изображению игрока
enemy_image = pygame.image.load("img/enemy.png")  # Замените на путь к вашему изображению врага
exit_image = pygame.image.load("img/exit.png")  # Замените на путь к вашему изображению выхода
yards_image = pygame.image.load("img/165.jpg")

# Размеры и позиции
player_rect = player_image.get_rect()
enemy_rect = enemy_image.get_rect()
exit_rect = exit_image.get_rect()

# Позиция игрока
player_rect.center = (400, 300)

# Позиция выхода
exit_rect.center = (400, 500)

# Сцены
class Scene:
    def __init__(self):
        self.running = True
        self.next_scene = None
        self.player = player_image
        self.exit = exit_image

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self, screen):
        pass

class MainScene(Scene):
    def __init__(self):
        super().__init__()
        self.enemies = []
        self.spawn_enemies()
        self.player_rect = player_rect
        self.exit_rect = exit_rect

    def spawn_enemies(self):
        for _ in range(5):  # Количество врагов
            enemy_rect = enemy_image.get_rect()
            enemy_rect.center = (random.randint(100, 700), random.randint(100, 500))
            self.enemies.append(enemy_rect)

    def handle_events(self, events):
        super().handle_events(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player_rect.x -= 5
                elif event.key == pygame.K_RIGHT:
                    self.player_rect.x += 5
                elif event.key == pygame.K_UP:
                    self.player_rect.y -= 5
                elif event.key == pygame.K_DOWN:
                    self.player_rect.y += 5

    def update(self):
        for enemy in self.enemies:
            if self.player_rect.colliderect(enemy):
                self.running = False
                self.next_scene = None
                return

        if self.player_rect.colliderect(self.exit_rect):
            self.running = False
            self.next_scene = SecondScene()

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Черный фон
        screen.blit(self.player, self.player_rect)
        screen.blit(self.exit, self.exit_rect)
        for enemy in self.enemies:
            screen.blit(enemy_image, enemy)

class SecondScene(Scene):
    def __init__(self):
        super().__init__()
        self.player_rect = player_rect
        self.exit_rect = exit_rect

    def handle_events(self, events):
        super().handle_events(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.running = False
                    self.next_scene = MainScene()

    def update(self):
        if self.player_rect.colliderect(self.exit_rect):
            self.running = False
            self.next_scene = None

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Черный фон
        screen.blit(self.player, self.player_rect)
        screen.blit(self.exit, self.exit_rect)

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

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()