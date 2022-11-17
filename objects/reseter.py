import pygame

from objects.controllable import Controllable


class Reseter(Controllable):
    def __init__(self, im, x, y, scr_size, manager):
        super().__init__(im, x, y, scr_size)

        self.manager = manager

    def control(self, event):
        if event.key == pygame.K_KP_ENTER:
            self.manager.objects.remove(self)
            self.manager.reset()
