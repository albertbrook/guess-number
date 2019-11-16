import pygame
from button import Button
from number import Number


class Functions(object):
    def __init__(self, settings, screen, buttons, numbers, guess):
        self.settings = settings
        self.screen = screen
        self.buttons = buttons
        self.numbers = numbers
        self.guess = guess

        self.create_button()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                for button in self.buttons:
                    if (0 < pos[0] - button.position[0] - button.moving_x < self.settings.button_size and
                            0 < pos[1] - button.position[1] - button.moving_y < self.settings.button_size):
                        num = self.find_num(button)
                        if not self.guess.flag:
                            if num == "R":
                                self.guess.start_random()
                            return
                        if num in range(1, 10) or num == 0:
                            if not str(self.guess.number.num).isdigit():
                                self.guess.number.num = num
                                return
                            self.guess.number.num *= 10
                            self.guess.number.num += num
                        elif num == "G":
                            self.guess.guess_number()

    def update_screen(self):
        self.buttons.update()
        self.numbers.update()

    def draw_screen(self):
        self.screen.fill((0, 0, 0))
        for button in self.buttons:
            button.draw()
        self.numbers.draw(self.screen)
        pygame.display.update()

    def create_button(self):
        num_list = [i for i in range(1, 10)]
        num_list += ["G", 0, "R"]
        index = 0
        for i in range(4):
            for j in range(3):
                position = (j * self.settings.button_size + (j + 1) * self.settings.button_gap,
                            (i + 1) * self.settings.button_size + (i + 2) * self.settings.button_gap)
                button = Button(self.settings, self.screen, position)
                button.add(self.buttons)
                number = Number(self.settings, self.screen, button, num_list[index])
                number.add(self.numbers)
                index += 1
        button = Button(self.settings, self.screen, (self.settings.button_gap, self.settings.button_gap))
        button.rect = pygame.Rect(button.position, self.settings.display_size)
        button.add(self.buttons)
        self.guess.number = Number(self.settings, self.screen, button, "Press R to start")
        self.guess.number.add(self.numbers)

    def find_num(self, button):
        for number in self.numbers:
            if number.button == button:
                return number.num
