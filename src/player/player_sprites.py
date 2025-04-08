from pathlib import Path
import pygame


# Функция для загрузки спрайтов с использованием pathlib
def load_sprite(filename, target_height):
    assets_path = Path(__file__).resolve().parent.parent.parent / "assets/sprites/"
    sprite_path = assets_path / filename

    if not sprite_path.exists():
        raise FileNotFoundError(f"Файл не найден: {sprite_path}")

    image = pygame.image.load(str(sprite_path)).convert_alpha()

    original_width, original_height = image.get_size()

    # Рассчитываем ширину пропорционально новой высоте
    aspect_ratio = original_width / original_height
    target_width = int(target_height * aspect_ratio)

    return pygame.transform.scale(image, (target_width, target_height))


class HeroSprites:
    def __init__(self, height):
        self.height = height

        # Спрайты для различных действий
        self.idle_images = [
            load_sprite(
                "hero1/idle/idle_frame_1.png",
                self.height,
            ),
            load_sprite(
                "hero1/idle/idle_frame_2.png",
                self.height,
            ),
            load_sprite(
                "hero1/idle/idle_frame_3.png",
                self.height,
            ),
            load_sprite(
                "hero1/idle/idle_frame_4.png",
                self.height,
            ),
            load_sprite(
                "hero1/idle/idle_frame_5.png",
                self.height,
            ),
            load_sprite(
                "hero1/idle/idle_frame_6.png",
                self.height,
            ),
            load_sprite(
                "hero1/idle/idle_frame_7.png",
                self.height,
            ),
            load_sprite(
                "hero1/idle/idle_frame_8.png",
                self.height,
            ),
            load_sprite(
                "hero1/idle/idle_frame_9.png",
                self.height,
            ),
            load_sprite(
                "hero1/idle/idle_frame_10.png",
                self.height,
            ),
            load_sprite(
                "hero1/idle/idle_frame_11.png",
                self.height,
            ),
            load_sprite(
                "hero1/idle/idle_frame_12.png",
                self.height,
            ),
            load_sprite(
                "hero1/idle/idle_frame_13.png",
                self.height,
            ),
            load_sprite(
                "hero1/idle/idle_frame_14.png",
                self.height,
            ),
            load_sprite(
                "hero1/idle/idle_frame_15.png",
                self.height,
            ),
        ]

        self.jump_images = [
            load_sprite(
                "hero1/jump/jump_frame_5.png",
                self.height,
            ),
            load_sprite(
                "hero1/jump/jump_frame_6.png",
                self.height,
            ),
            load_sprite(
                "hero1/jump/jump_frame_7.png",
                self.height,
            ),
            load_sprite(
                "hero1/jump/jump_frame_8.png",
                self.height,
            ),
            load_sprite(
                "hero1/jump/jump_frame_9.png",
                self.height,
            ),
            load_sprite(
                "hero1/jump/jump_frame_10.png",
                self.height,
            ),
            load_sprite(
                "hero1/jump/jump_frame_11.png",
                self.height,
            ),
            load_sprite(
                "hero1/jump/jump_frame_12.png",
                self.height,
            ),
            load_sprite(
                "hero1/jump/jump_frame_13.png",
                self.height,
            ),
            load_sprite(
                "hero1/jump/jump_frame_14.png",
                self.height,
            ),
        ]
        self.attack_images = [
            load_sprite(
                "hero1/attacks/attack_frame_1.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_2.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_3.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_4.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_5.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_6.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_7.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_8.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_9.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_10.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_11.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_12.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_13.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_14.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_15.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_16.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_17.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_18.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_19.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_20.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_21.png",
                self.height,
            ),
            load_sprite(
                "hero1/attacks/attack_frame_22.png",
                self.height,
            ),
        ]
        self.defend_images = [
            load_sprite(
                "hero1/defend/defend_frame_1.png",
                self.height,
            ),
            load_sprite(
                "hero1/defend/defend_frame_2.png",
                self.height,
            ),
            load_sprite(
                "hero1/defend/defend_frame_3.png",
                self.height,
            ),
            load_sprite(
                "hero1/defend/defend_frame_4.png",
                self.height,
            ),
            load_sprite(
                "hero1/defend/defend_frame_5.png",
                self.height,
            ),
            load_sprite(
                "hero1/defend/defend_frame_6.png",
                self.height,
            ),
        ]
        self.hurt_images = [
            load_sprite(
                "hero/hurt/hurt_frame_1.png",
                self.height,
            ),
            load_sprite(
                "hero/hurt/hurt_frame_2.png",
                self.height,
            ),
        ]
        self.death_images = [
            load_sprite(
                "hero1/death/death_frame_1.png",
                self.height,
            ),
            load_sprite(
                "hero1/death/death_frame_2.png",
                self.height,
            ),
            load_sprite(
                "hero1/death/death_frame_3.png",
                self.height,
            ),
            load_sprite(
                "hero1/death/death_frame_4.png",
                self.height,
            ),
            load_sprite(
                "hero1/death/death_frame_5.png",
                self.height,
            ),
            load_sprite(
                "hero1/death/death_frame_6.png",
                self.height,
            ),
            load_sprite(
                "hero1/death/death_frame_7.png",
                self.height,
            ),
            load_sprite(
                "hero1/death/death_frame_8.png",
                self.height,
            ),
            load_sprite(
                "hero1/death/death_frame_9.png",
                self.height,
            ),
            load_sprite(
                "hero1/death/death_frame_10.png",
                self.height,
            ),
            load_sprite(
                "hero1/death/death_frame_11.png",
                self.height,
            ),
            load_sprite(
                "hero1/death/death_frame_12.png",
                self.height,
            ),
            load_sprite(
                "hero1/death/death_frame_13.png",
                self.height,
            ),
            load_sprite(
                "hero1/death/death_frame_14.png",
                self.height,
            ),
        ]

        self.run_images = [
            load_sprite(
                "hero1/run/run_frame_1.png",
                self.height,
            ),
            load_sprite(
                "hero1/run/run_frame_2.png",
                self.height,
            ),
            load_sprite(
                "hero1/run/run_frame_3.png",
                self.height,
            ),
            load_sprite(
                "hero1/run/run_frame_4.png",
                self.height,
            ),
            load_sprite(
                "hero1/run/run_frame_5.png",
                self.height,
            ),
            load_sprite(
                "hero1/run/run_frame_6.png",
                self.height,
            ),
            load_sprite(
                "hero1/run/run_frame_7.png",
                self.height,
            ),
            load_sprite(
                "hero1/run/run_frame_8.png",
                self.height,
            ),
        ]

        # self.attack_run_images = [
        #     load_sprite(
        #         "hero/attack_run/frame_attack_1.png",
        #         self.height,
        #     ),
        #     load_sprite(
        #         "hero/attack_run/frame_attack_2.png",
        #         self.height,
        #     ),
        #     load_sprite(
        #         "hero/attack_run/frame_attack_3.png",
        #         self.height,
        #     ),
        #     load_sprite(
        #         "hero/attack_run/frame_attack_4.png",
        #         self.height,
        #     ),
        #     load_sprite(
        #         "hero/attack_run/frame_attack_5.png",
        #         self.height,
        #     ),
        #     load_sprite(
        #         "hero/attack_run/frame_attack_6.png",
        #         self.height,
        #     ),
        # ]
