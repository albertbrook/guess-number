import random
import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, settings, screen, position):
        super().__init__()
        self.settings = settings
        self.screen = screen

        self.position = position
        self.color = None
        self.rect = pygame.Rect(self.position, (self.settings.button_size, self.settings.button_size))

        self.moving_x = random.randint(-self.settings.random_moving_range, self.settings.random_moving_range)
        self.moving_y = random.randint(-self.settings.random_moving_range, self.settings.random_moving_range)

        self.update()

    def update(self):
        self.color = tuple([random.randint(0, 255) for _ in range(3)])
        self.rect.x += self.moving_x
        self.rect.y += self.moving_y
        self.moving_x = -self.moving_x
        self.moving_y = -self.moving_y

    def draw(self):
        self.screen.fill(self.color, self.rect)
