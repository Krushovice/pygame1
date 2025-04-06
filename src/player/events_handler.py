from pygame.locals import *


# Обработчик событий
def handle_events(events, running, player):
    for event in events:
        if event.type == QUIT:
            running = False

        # Обработка нажатий клавиш
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_LEFT:
                player.move_left()
            elif event.key == K_RIGHT:
                player.move_right()
            elif event.key == K_UP:
                player.jump()  # Прыжок по клавише "Вверх"

            elif event.key == K_SPACE:
                player.defend()  # Защита по клавише "Z"

        # Обработка отпускания клавиш
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                player.is_running = (
                    False  # Останавливаем движение при отпускании клавиши
                )
            elif event.key == K_SPACE:
                player.stop_defend()  # Останавливаем защиту

        # Обработка нажатия левой кнопки мыши для атаки
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши (button == 1)
                if not player.is_attacking:  # Если атака еще не активна
                    player.attack()  # Вызываем метод атаки
                player.is_attacking = True  # Устанавливаем флаг атаки

        # Обработка отпускания левой кнопки мыши для завершения атаки
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:  # Левая кнопка мыши (button == 1)
                player.stop_attack()  # Завершаем атаку при отпускании кнопки

    return running
