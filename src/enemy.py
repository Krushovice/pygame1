import pygame

class Enemy:
    def __init__(self,
                 x: int,
                 y: int,
                 width: int = 35,
                 height: int = 40,
        ):
        self.x = x  # Начальная позиция по оси X
        self.y = y  # Начальная позиция по оси Y (по умолчанию для земли на уровне Y=500)
        self.width = width  # Ширина врага
        self.height = height  # Высота врага
        self.speed = 3
        self.health = 80
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 128, 0))  # Зеленый, как орк

        # Устанавливаем врага на землю (координата Y на уровне земли)
        self.y = 500 - self.height  # Корректируем Y, чтобы враг стоял на земле

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        # Пока враг не будет прыгать или изменять высоту, ось Y не изменяется
        # self.y остается на уровне земли.

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

