class Settings(object):
    def __init__(self):
        self.frames_per_second = 64

        self.button_size = 100
        self.button_gap = 50

        self.display_size = (self.button_size * 3 + self.button_gap * 2, self.button_size)

        self.screen_size = (self.button_size * 3 + self.button_gap * 4,
                            self.button_size * 5 + self.button_gap * 6)

        self.font_size = 72

        self.random_moving_range = 10

        self.random_range = (1, 100)
