from objects.gameobject import GameObject


class Controllable(GameObject):
    def __init__(self, im, x, y, scr_size):
        super().__init__(im, x, y, scr_size)

    def control(self, event):
        pass
