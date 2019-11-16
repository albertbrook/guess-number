import pygame
from functions import Functions
from settings import Settings
from guess import Guess


class Game(object):
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption("Guess Number")

        self.buttons = pygame.sprite.Group()
        self.numbers = pygame.sprite.Group()
        self.guess = Guess(self.settings)

        self.functions = Functions(self.settings, self.screen, self.buttons, self.numbers, self.guess)

    def start(self):
        while True:
            pygame.time.Clock().tick(self.settings.frames_per_second)
            self.functions.check_events()
            self.functions.update_screen()
            self.functions.draw_screen()


if __name__ == '__main__':
    game = Game()
    game.start()
