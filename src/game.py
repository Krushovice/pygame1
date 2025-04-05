import pygame
from player import Player
from enemy import Enemy

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60

# Создание окна игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My RPG Game")

# Главный игровой цикл
def main():
    clock = pygame.time.Clock()
    player = Player(x=100, y=100)
    enemy = Enemy(300, 85)

    running = True
    while running:
        screen.fill((0, 0, 0))  # Очистка экрана

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Движение и атаки
        player.update()
        enemy.update()

        # Отображение игрока и врага
        player.draw(screen)
        enemy.draw(screen)

        # Обновление экрана
        pygame.display.flip()

        # Установка FPS
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
