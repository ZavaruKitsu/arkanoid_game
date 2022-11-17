import pygame

from logger import logger
from objects.gameobject import GameObject

# ---------------------------------------------------------------------------- #
#                                   CONSTANTS                                  #
# ---------------------------------------------------------------------------- #

SIZE = WIDTH, HEIGHT = 1600, 960

BACKGROUND = 103, 58, 183

BACKGROUND_IMAGE = 'assets/background.jpg'
PLATFORM_IMAGE = 'assets/platform.png'
BALL_IMAGE = 'assets/ball.png'
ENEMY_IMAGE = 'assets/enemy.png'


class GameManager:
    def __init__(self, objects):
        self.font = pygame.font.Font(None, 48)

        self.objects = objects
        self.score = 0
        self.lost = False
        self.score_surface = None

    def create_objects(self):
        from objects.ball import Ball
        from objects.enemy import Enemy
        from objects.platform import Platform

        if not self in self.objects:
            self.objects.append(self)

        background_img = pygame.transform.scale(
            pygame.image.load(BACKGROUND_IMAGE), SIZE)
        background = GameObject(background_img, 0, 0, SIZE)
        self.objects.append(background)

        platform_img = pygame.image.load(PLATFORM_IMAGE)
        player = Platform(platform_img, WIDTH // 2, HEIGHT - 30, SIZE)
        self.objects.append(player)

        ball_img_load = pygame.image.load(BALL_IMAGE)
        ball_img = pygame.transform.scale(ball_img_load, (64, 64))
        ball = Ball(ball_img, WIDTH // 2,
                    800, SIZE, self.objects)
        self.objects.append(ball)

        # Enemy generation step
        enemy_img_load = pygame.image.load(ENEMY_IMAGE)
        enemy_img = pygame.transform.scale(enemy_img_load, (64, 64))

        for i in range(3):
            for j in range(15):
                enemy = Enemy(enemy_img, j * 64 + j * 64, i * 200 + i * 20, SIZE, self.objects)
                self.objects.append(enemy)

        img = self.font.render(f'Score: {self.score}', True, (255, 144, 0))
        self.score_surface = GameObject(img, SIZE[0] - 200, SIZE[1] - 100, SIZE)
        self.objects.append(self.score_surface)

    def increase_score(self):
        self.score += 1

        img = self.font.render(f'Score: {self.score}', True, (255, 144, 0))
        self.score_surface.image = img

    def loose(self):
        from objects.reseter import Reseter

        self.lost = True
        self.objects.clear()

        logger.warning('lost')

        # bigger font
        font = pygame.font.Font(None, 96)
        img = font.render(f'Score: {self.score}', True, (255, 144, 0))
        self.objects.append(GameObject(img, WIDTH // 2 - 192, HEIGHT // 2 + 192, SIZE))
        self.objects.append(Reseter(None, None, None, None, self))

    def reset(self):
        logger.warning('reset')

        self.score = 0
        self.lost = False

        self.create_objects()
