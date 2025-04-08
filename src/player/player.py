import pygame
import os

from dotenv import load_dotenv

from .player_sprites import HeroSprites


load_dotenv()


class Player:
    def __init__(self, x, height=190):
        self.x = x
        self.y = 500 - height
        self.height = height
        self.speed = 10
        self.run_speed = 15
        self.health = 100
        self.screen_width = int(os.getenv("SCREEN_WIDTH"))

        self.gravity = 1
        self.jump_power = -15
        self.is_jumping = False
        self.on_ground = True
        self.velocity_y = 0

        self.is_running = False
        self.is_walking = False
        self.is_attacking = False
        self.is_blocking = False

        self.animation_speed = 0.0171
        self.animation_timer = 0
        self.image_index = 0

        self.sprites = HeroSprites(self.height)
        # Получаем ширину из первого idle-кадра (например)
        self.width = self.sprites.idle_images[0].get_width()
        self.current_image = self.sprites.idle_images[0]

    def update(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0

            # if self.is_running and self.is_attacking:
            #     self.image_index = (self.image_index + 1) % len(
            #         self.sprites.attack_run_images
            #     )
            #     self.current_image = self.sprites.attack_run_images[self.image_index]

            if self.is_running:
                self.image_index = (self.image_index + 1) % len(self.sprites.run_images)
                self.current_image = self.sprites.run_images[self.image_index]

            # elif self.is_walking:
            #     self.image_index = (self.image_index + 1) % len(
            #         self.sprites.walk_images
            #     )
            #     self.current_image = self.sprites.walk_images[self.image_index]

            elif self.is_jumping:
                self.current_image = self.sprites.jump_images[0]

            elif self.is_attacking:
                self.image_index = (self.image_index + 1) % len(
                    self.sprites.attack_images
                )
                self.current_image = self.sprites.attack_images[self.image_index]
                self.x += 5

            elif self.is_blocking:
                self.image_index = (self.image_index + 1) % len(
                    self.sprites.defend_images
                )
                self.current_image = self.sprites.defend_images[self.image_index]

            else:
                self.image_index = (self.image_index + 1) % len(
                    self.sprites.idle_images
                )
                self.current_image = self.sprites.idle_images[self.image_index]
        # Ограничение по оси X (не выходим за экран)
        if self.x < 0:
            self.x = 0  # Не даем выйти за левую границу экрана
        elif self.x + self.width + 1 > self.screen_width:
            self.x = (
                self.screen_width - self.width
            )  # Не даем выйти за правую границу экрана

        if self.is_jumping:
            self.velocity_y += self.gravity
            self.y += self.velocity_y
            if self.y >= 500 - self.height:
                self.y = 500 - self.height
                self.is_jumping = False
                self.on_ground = True
                self.velocity_y = 0
        else:
            self.velocity_y = 0

    def move_left(self, is_running=False):
        if is_running:
            self.x -= self.run_speed
            self.is_running = True
            self.is_walking = False
        else:
            self.x -= self.speed
            self.is_walking = True
            self.is_running = False

    def move_right(self, is_running=False):
        if is_running:
            self.x += self.run_speed
            self.is_running = True
            self.is_walking = False
        else:
            self.x += self.speed
            self.is_walking = True
            self.is_running = False

    def stop_move(self):
        self.is_running = False
        self.is_walking = False

    def jump(self):
        if self.on_ground:
            self.is_jumping = True
            self.on_ground = False
            self.velocity_y = self.jump_power

    def attack(self):
        if not self.is_attacking:
            self.is_attacking = True
            pygame.time.set_timer(pygame.USEREVENT, 500)

    def stop_attack(self):
        self.is_attacking = False

    def block(self):
        self.is_blocking = True

    def stop_block(self):
        self.is_blocking = False

    def draw(self, screen):
        screen.blit(self.current_image, (self.x, self.y))
