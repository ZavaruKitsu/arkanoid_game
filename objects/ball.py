import pygame

from objects.gamemanager import GameManager
from objects.interactable import Interactable
from objects.platform import Platform


class Ball(Interactable):
    def __init__(self, im, x, y, scr_size, objects):
        super().__init__(im, x, y, scr_size, objects)

        self.dir_x = -1
        self.dir_y = 1

        self.original_image = self.image.copy()
        self.angle = 1

        self.player = self.get_object(lambda x: isinstance(x, Platform))

    def move(self):
        self.angle -= 1 % 360 * self.dir_x

        self.image = self.rotate_image(self.angle)
        self.pos = self.pos.move(self.dir_x, self.dir_y)

        if self.pos.right > self.scr_width:
            self.dir_x *= -1

        if self.pos.top > self.scr_height - self.pos.height:
            self.dir_y *= -1

        if self.pos.left < 0:
            self.dir_x *= -1

        if self.pos.bottom < self.pos.height:
            self.dir_y *= -1

    def interact(self):
        player_col = self.player.pos.colliderect(self.pos)
        bottom_col = self.pos.top > self.scr_height - self.pos.height

        if not player_col and not bottom_col:
            return

        if player_col:
            self.dir_y *= -1
            return

        if bottom_col:
            self.get_object(lambda x: isinstance(x, GameManager)).loose()

    def rotate_image(self, angle):
        orig_rect = self.original_image.get_rect()

        rot_image = pygame.transform.rotate(self.original_image, angle)

        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center

        rot_image = rot_image.subsurface(rot_rect).copy()

        return rot_image
