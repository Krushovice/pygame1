from pygame.locals import *


def handle_events(events, running, player):
    for event in events:
        if event.type == QUIT:
            running = False

        # Нажатие клавиш
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_a:
                player.move_left(is_running=True)
            elif event.key == K_d:
                player.move_right(is_running=True)
            elif event.key == K_SPACE:
                player.jump()

        # Отпускание клавиш
        elif event.type == KEYUP:
            if event.key == K_a or event.key == K_d:
                player.stop_move()  # вызываем отдельный метод для сброса состояния

        # Левая кнопка мыши (атака)
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            player.attack()

        elif event.type == MOUSEBUTTONUP and event.button == 1:
            player.stop_attack()

        # Правая кнопка мыши (блокировка)
        elif event.type == MOUSEBUTTONDOWN and event.button == 3:
            player.block()

        elif event.type == MOUSEBUTTONUP and event.button == 3:
            player.stop_block()

    return running
