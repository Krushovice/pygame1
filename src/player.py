import pygame

class Player:
    def __init__(self, x, y, width=30, height=30):
        self.x = x  # Начальная позиция по оси X
        self.y = y  # Начальная позиция по оси Y (по умолчанию для земли на уровне Y=500)
        self.width = width  # Ширина
        self.height = height  # Высота
        self.speed = 5
        self.health = 100
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 0, 0))  # Красный

        # Устанавливаем врага на землю (координата Y на уровне земли)
        self.y = 500 - self.height  # Корректируем Y, чтобы враг стоял на земле

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        # self.y остается на уровне земли.

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

