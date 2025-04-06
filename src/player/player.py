import pygame

from .player_sprites import HeroSprites


class Player:
    def __init__(self, x, y, width=255, height=185):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 10
        self.health = 100

        # Переменные для прыжка, гравитации и проверки нахождения на земле
        self.gravity = 1  # Гравитация
        self.jump_power = -15  # Сила прыжка
        self.is_jumping = False
        self.on_ground = True  # На земле или нет
        self.velocity_y = 0  # Вертикальная скорость

        # Логика для атаки и защиты
        self.is_attacking = False
        self.is_defending = False

        # Загружаем спрайты героя
        self.sprites = HeroSprites(self.width, self.height)
        self.current_image = self.sprites.idle_images[0]  # Начальное изображение
        self.animation_speed = 0.1
        self.animation_timer = 0
        self.image_index = 0

        # Состояния движения
        self.is_running = False

    def update(self, dt):
        # Логика анимации
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            # Обновляем кадры в зависимости от состояния
            if self.is_running:
                self.image_index = (self.image_index + 1) % len(
                    self.sprites.walk_images
                )
                self.current_image = self.sprites.walk_images[self.image_index]
            elif self.is_jumping:
                self.current_image = self.sprites.jump_images[0]  # Один кадр для прыжка
            elif self.is_attacking:
                self.image_index = (self.image_index + 1) % len(
                    self.sprites.attack_images
                )
                self.current_image = self.sprites.attack_images[self.image_index]
            elif self.is_defending:
                self.image_index = (self.image_index + 1) % len(
                    self.sprites.defend_images
                )
                self.current_image = self.sprites.defend_images[self.image_index]
            else:
                self.image_index = (self.image_index + 1) % len(
                    self.sprites.idle_images
                )
                self.current_image = self.sprites.idle_images[self.image_index]

        # Логика гравитации и прыжка
        if self.is_jumping:
            self.velocity_y += self.gravity  # Применяем гравитацию
            self.y += self.velocity_y

            # Проверяем, не достиг ли игрок земли
            if self.y >= 500 - self.height:  # Уровень земли на Y=500
                self.y = 500 - self.height  # Фиксируем персонажа на земле
                self.is_jumping = False  # Прекращаем прыжок
                self.on_ground = True  # Игрок теперь на земле
                self.velocity_y = 0  # Обнуляем вертикальную скорость
        else:
            self.velocity_y = 0  # Если на земле, сбрасываем вертикальную скорость

    def move_left(self):
        self.x -= self.speed
        self.is_running = True

    def move_right(self):
        self.x += self.speed
        self.is_running = True

    def jump(self):
        if self.on_ground:  # Можно прыгать только если персонаж на земле
            self.is_jumping = True
            self.on_ground = False  # Игрок не на земле
            self.velocity_y = self.jump_power  # Применяем силу прыжка

    def attack(self):
        if not self.is_attacking:  # Атакуем только если не атакуем в данный момент
            self.is_attacking = True
            # Вставьте сюда логику атаки (например, проверка на попадание по врагу)
            pygame.time.set_timer(
                pygame.USEREVENT, 400
            )  # Таймер для завершения атаки после 500 мс

    def stop_attack(self):
        self.is_attacking = False  # Завершаем атаку

    def defend(self):
        self.is_defending = True

    def stop_defend(self):
        self.is_defending = False

    def draw(self, screen):
        screen.blit(self.current_image, (self.x, self.y))
