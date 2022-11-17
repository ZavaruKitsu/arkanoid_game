class GameObject:

    def __init__(self, im, x, y, scr_size):
        if not im:
            return
        self.image = im
        self.pos = im.get_rect().move(x, y)
        self.scr_width = scr_size[0]
        self.scr_height = scr_size[1]

    def move(self):
        pass
