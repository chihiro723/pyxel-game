import pyxel
import random #32 8
from info2_Home import Home
from info2_Game import Game
from info2_Change import Change

class App:
    def __init__(self):
        pyxel.init(256, 256)
        self.current_character = random.choice(["monkey", "chicken", "dog", "owl"])
        self.state = 'home'
        self.home = Home(self.current_character)
        self.game = None
        self.change = None
        
    def update(self):
        if self.state == 'home':
            self.home.update()
            if self.home.change_to_game:
                self.state = 'game'
                self.game = Game(self.current_character)
            elif self.home.change_to_change:
                self.state = 'change'
                self.change = Change(self.current_character)
        elif self.state == 'change':
            self.change.update()
            if self.change.change_to_home:
                self.state = 'home'
                self.current_character = self.change.current_character
                self.home = Home(self.current_character)

        elif self.state == 'game':
            self.game.update()
            if self.game.change_to_home:
                self.state = 'home'
                self.home = Home(self.current_character)

    def draw(self):
        if self.state == 'home':
            self.home.draw()
        if self.state == 'change':
            self.change.draw()
        elif self.state == 'game':
            self.game.draw()

    def run(self):
        pyxel.run(self.update, self.draw)

if __name__ == "__main__":
    app = App()
    app.run()