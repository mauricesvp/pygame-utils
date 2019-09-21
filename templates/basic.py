# github.com/mauricesvp
# if all else fails: https://www.pygame.org/docs/

import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_ESCAPE

import time

WIN_HEIGHT = 800
WIN_WIDTH = 800

TICK = 0.1


class App:
    def __init__(self):
        self.display_surface = None
        self.running = True
        self.counter = 0

    def on_init(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.HWSURFACE)
        pygame.display.set_caption("abc")

    def on_render(self):
        # Background
        self.display_surface.fill((100, 100, 100))

        # Update Screen
        pygame.display.flip()

    def on_loop(self):
        pass

    def on_execute(self):
        self.on_init()

        while self.running:
            pygame.event.pump()
            key_press = pygame.key.get_pressed()

            if key_press[K_LEFT]:
                pass
            if key_press[K_RIGHT]:
                pass
            if key_press[K_ESCAPE]:
                self.running = False
                exit()

            self.on_loop()
            self.on_render()

            time.sleep(TICK)
            self.counter += 1


def main():
    game_app = App()
    game_app.on_execute()


if __name__ == "__main__":
    main()
