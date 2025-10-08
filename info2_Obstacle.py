import pyxel
import random

class Obstacle:
    def __init__(self):
        self.width = 16  
        self.height = 16 
        self.reset()

    def reset(self):
        self.x = 0 if random.choice([True, False]) else pyxel.width
        self.y = random.randint(10, pyxel.height - 10)
        self.speed = 2 if self.x == 0 else -2
        self.active = True

    def update(self):
        if self.active:
            self.x += self.speed
            if self.x < -self.width or self.x > pyxel.width:
                self.active = False

    def draw(self):
        if self.active:
            pyxel.blt(self.x, self.y, 0, 16, 8, 16, 16, 3)

    def collides_with_player(self, player):
        player_left = player.x
        player_right = player.x + player.width
        player_top = player.y
        player_bottom = player.y + player.height

        ball_left = self.x - self.width
        ball_right = self.x + self.width
        ball_top = self.y - self.height
        ball_bottom = self.y + self.height

        return (ball_right > player_left and
                ball_left < player_right and
                ball_bottom > player_top and
                ball_top < player_bottom)