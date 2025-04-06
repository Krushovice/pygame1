import pygame


class Enemy:
    def __init__(
        self,
        x: int,
        y: int,
        width: int = 125,
        height: int = 95,
    ):
        self.x = x  # Начальная позиция по оси X
        self.y = (
            y  # Начальная позиция по оси Y (по умолчанию для земли на уровне Y=500)
        )
        self.width = width  # Ширина врага
        self.height = height  # Высота врага
        self.speed = 3
        self.health = 80

        self.image = pygame.image.load("../assets/sprites/orc_sprite.png")
        self.image = pygame.transform.scale(
            self.image,
            (self.width, self.height),
        )  # Масштабируем изображение под размер героя

        # Устанавливаем врага на землю (координата Y на уровне земли)
        self.y = 500 - self.height  # Корректируем Y, чтобы враг стоял на земле

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
