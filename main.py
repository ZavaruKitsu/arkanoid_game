import time

from logger import logger
from objects.gamemanager import GameManager, SIZE
from objects.interactable import *
from objects.platform import *

TITLE = 'Arkanoid game | by ZavaruKitsu'

# ---------------------------------------------------------------------------- #
#                                INITIALIZATION                                #
# ---------------------------------------------------------------------------- #

pygame.init()
pygame.display.set_caption(TITLE)

game_objects = []
manager = GameManager(game_objects)
game_objects.append(manager)

screen = pygame.display.set_mode(SIZE)

manager.create_objects()

exit_requested = False

logger.info('initialization done')

# ---------------------------------------------------------------------------- #
#                                     GAME                                     #
# ---------------------------------------------------------------------------- #

while not exit_requested:

    # ---------------------------------------------------------------------------- #
    #                                 KEY HANDLERS                                 #
    # ---------------------------------------------------------------------------- #

    for event in pygame.event.get():
        if event.type not in (pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP):
            continue

        logger.info('input detected:', event)

        if event.type == pygame.QUIT:
            exit_requested = True
            break
        else:
            for item in game_objects:
                if isinstance(item, Controllable):
                    item.control(event)

    # ---------------------------------------------------------------------------- #
    #                                    UPDATE                                    #
    # ---------------------------------------------------------------------------- #

    # time before screen update
    time.sleep(0.0015)

    for item in game_objects:
        if not isinstance(item, GameObject):
            continue

        item.move()

        if isinstance(item, Interactable):
            item.interact()

        if hasattr(item, 'image'):
            screen.blit(item.image, item.pos)

    pygame.display.flip()

pygame.quit()
logger.warning('done')
