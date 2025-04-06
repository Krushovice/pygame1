from pathlib import Path
import pygame


# Функция для загрузки спрайтов с использованием pathlib
def load_sprite(filename, width, height):
    # Получаем путь к текущей директории и переходим в папку "assets"
    assets_path = (
        Path(__file__).resolve().parent.parent.parent / "assets/sprites/"
    )  # Идём на 2 уровня выше (src и проект)

    # Формируем полный путь к изображению
    sprite_path = assets_path / filename

    # Проверяем, существует ли файл
    if not sprite_path.exists():
        raise FileNotFoundError(f"Файл не найден: {sprite_path}")

    # Преобразуем путь в строку
    sprite_path = str(sprite_path)

    # Загружаем изображение
    image = pygame.image.load(sprite_path)

    # Масштабируем изображение
    return pygame.transform.scale(image, (width, height))


class HeroSprites:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Спрайты для различных действий
        self.idle_images = [
            load_sprite(
                "hero/idle/idle_frame_1.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/idle/idle_frame_2.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/idle/idle_frame_3.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/idle/idle_frame_4.png",
                self.width,
                self.height,
            ),
        ]
        self.walk_images = [
            load_sprite(
                "hero/walk/walk_frame_1.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/walk/walk_frame_2.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/walk/walk_frame_3.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/walk/walk_frame_4.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/walk/walk_frame_5.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/walk/walk_frame_6.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/walk/walk_frame_7.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/walk/walk_frame_8.png",
                self.width,
                self.height,
            ),
        ]
        self.jump_images = [
            load_sprite(
                "hero/jump/jump_frame_1.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/jump/jump_frame_2.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/jump/jump_frame_3.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/jump/jump_frame_4.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/jump/jump_frame_5.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/jump/jump_frame_6.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/jump/jump_frame_7.png",
                self.width,
                self.height,
            ),
        ]
        self.attack_images = [
            load_sprite(
                "hero/attacks/attack_frame_1.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/attacks/attack_frame_2.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/attacks/attack_frame_3.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/attacks/attack_frame_4.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/attacks/attack_frame_5.png",
                self.width,
                self.height,
            ),
        ]
        self.defend_images = [
            load_sprite(
                "hero/defend/defend_frame_1.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/defend/defend_frame_2.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/defend/defend_frame_3.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/defend/defend_frame_4.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/defend/defend_frame_5.png",
                self.width,
                self.height,
            ),
        ]
        self.hurt_images = [
            load_sprite(
                "hero/hurt/hurt_frame_1.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/hurt/hurt_frame_2.png",
                self.width,
                self.height,
            ),
        ]
        self.death_images = [
            load_sprite(
                "hero/death/death_frame_1.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/death/death_frame_2.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/death/death_frame_3.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/death/death_frame_4.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/death/death_frame_5.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/death/death_frame_6.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/death/death_frame_7.png",
                self.width,
                self.height,
            ),
            load_sprite(
                "hero/death/death_frame_8.png",
                self.width,
                self.height,
            ),
        ]
