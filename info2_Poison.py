import pyxel
import random

class Poison:
    def __init__(self):
        self.poison_height = -40
        self.target_height = self.get_random_height()

    def update(self):
        if self.poison_height < self.target_height:
            self.poison_height += 0.5
        elif self.poison_height > self.target_height:
            self.poison_height -= 0.5

        if abs(self.poison_height - self.target_height) < 1:
            self.target_height = self.get_random_height()

    def draw(self):
        pyxel.rect(0, pyxel.height - self.poison_height, pyxel.width, self.poison_height, 8)

    def get_random_height(self):
        return random.uniform(pyxel.height * 0.1, pyxel.height * 0.8)