from objects.ball import Ball
from objects.gamemanager import GameManager
from objects.interactable import Interactable


class Enemy(Interactable):
    def __init__(self, im, x, y, scr_size, objects):
        super().__init__(im, x, y, scr_size, objects)

        self.ball = self.get_object(lambda pred: isinstance(pred, Ball))

    def interact(self):
        if not self.ball.pos.colliderect(self.pos):
            return

        self.objects.remove(self)

        self.ball.dir_x *= -1
        self.ball.dir_y *= -1

        self.get_object(lambda pred: isinstance(pred, GameManager)).increase_score()
