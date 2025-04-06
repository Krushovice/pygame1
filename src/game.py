import os

import pygame

from player.player import Player
from enemy.enemy import Enemy
from player.events_handler import handle_events

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60

# Создание окна игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ghosts of War")


# Главный игровой цикл
def main():
    clock = pygame.time.Clock()

    player = Player(x=100, y=350)
    # enemy = Enemy(300, 85)

    background = pygame.image.load("../data/levels/battleback5.png")

    music = pygame.mixer.Sound("../assets/sounds/city_sky.ogg")

    running = True
    while running:
        dt = clock.tick(60) / 1000

        screen.fill((0, 0, 0))  # Очистка экрана

        screen.blit(background, (0, 0))

        music.play()

        # Обработка событий
        running = handle_events(
            events=pygame.event.get(),
            running=running,
            player=player,
        )

        # Движение и атаки
        player.update(dt)
        # enemy.update()

        # Отображение игрока и врага
        player.draw(screen)
        # enemy.draw(screen)

        # Обновление экрана
        pygame.display.flip()

        # Установка FPS
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
