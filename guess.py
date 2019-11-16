import random


class Guess(object):
    def __init__(self, settings):
        self.settings = settings

        self.random_num = None
        self.number = None
        self.flag = False

    def start_random(self):
        self.random_num = random.randint(self.settings.random_range[0], self.settings.random_range[1])
        self.number.num = "Guess 1 to 100"
        self.flag = True

    def guess_number(self):
        if not str(self.number.num).isdigit():
            return
        if self.number.num > self.random_num:
            self.number.num = "too big"
        elif self.number.num < self.random_num:
            self.number.num = "too small"
        else:
            self.number.num = "congratulations"
            self.flag = False
