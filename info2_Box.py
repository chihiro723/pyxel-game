import pyxel
import random

class Box:
    def __init__(self):
        self.width = 30
        self.height = 4
        self.color = random.choice((8, 12 ,10))
        self.x = random.randint(0, 236)
        self.y = 0

    def create(self, start):
        self.y = random.randint(start - 70, start)
        
    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, self.color)

    def scroll(self):
        self.y += 0.7
    