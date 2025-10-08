import pyxel
import random

class Heal:
    def __init__(self):
        pyxel.load("heal.pyxres") # 仮のファイル
        self.x = random.randint(128, 256) #画面上半分の範囲ににx座標を設定
        self.y = random.randint(0, 256)

    def create(self):
        pyxel.blt(self.x, self.y, 0, 0, 8, 16, 16, 0) # 仮の値

    def scroll(self):
        self.y += 0.7 #ボックスと連動して動かす

    