import random
import pygame


class Number(pygame.sprite.Sprite):
    def __init__(self, settings, screen, button, num):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.button = button

        self.num = num
        self.color = None
        self.image = None
        self.rect = None

        self.font = pygame.font.SysFont(None, self.settings.font_size)

        self.update()

    def update(self):
        self.color = tuple([random.randint(0, 255) for _ in range(3)])
        self.image = self.font.render(str(self.num), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.button.rect.center
