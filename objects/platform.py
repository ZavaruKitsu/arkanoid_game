import pygame

from objects.controllable import Controllable

LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT


class Platform(Controllable):

    def __init__(self, im, x, y, scr_size):
        super().__init__(im, x, y, scr_size)

        self.dir = 0

    def move(self):
        save_pos = self.pos
        self.pos = self.pos.move(3 * self.dir, 0)

        if self.pos.right > self.scr_width or self.pos.left < 0:
            self.pos = save_pos

    def set_dir(self, dir):
        if dir not in (-1, 0, 1):
            return
        self.dir = dir

    def control(self, event):
        if event.type not in (pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP):
            return

        if event.type == pygame.KEYUP:
            if event.key in (LEFT_KEY, RIGHT_KEY):
                self.set_dir(0)
            return

        if event.key == LEFT_KEY:
            self.set_dir(-1)
        elif event.key == RIGHT_KEY:
            self.set_dir(1)
