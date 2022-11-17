from objects.gameobject import GameObject


class Interactable(GameObject):
    def __init__(self, im, x, y, scr_size, objects):
        super().__init__(im, x, y, scr_size)

        self.objects = objects

    def interact(self):
        pass

    def get_object(self, predicate):
        for item in self.objects:
            if predicate(item):
                return item
        raise KeyError
