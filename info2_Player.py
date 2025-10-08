import pyxel

class Player:
    def __init__(self):
        self.x = 128
        self.y = 214
        self.vy = 0
        self.vx = 0
        self.width = 3
        self.height = 12
        self.current_box_color = ""
        self.red = 1  # 赤色の踏み台のときにvxにかける重み
        self.blue = False  # 青色の踏み台のときに二段ジャンプを可能にする
        self.on_box = False  # 踏み台にいるかどうか
        self.last_input_time = 0
        self.input_cooldown = 7  # 入力無視期間

    def update(self, boxes):
        self.y -= self.vy
        self.vy -= 1
        self.x += self.vx

        # 踏み台との衝突判定
        self.on_box = False  # デフォルトでは踏み台にいないとする
        if self.vy < 0:
            for box in boxes:
                if self._collides_with_box(box):
                    self.y = box.y - self.height
                    self.vy = -2
                    self.on_box = True
                    self.current_box_color = box.color
                    # 踏み台に着地した
                    break

        if self.y > 214:
            self.y = 214
            self.vy = 0
        self.x = max(0, min(self.x, pyxel.width - self.width))

    def jump(self):
        # 地面または踏み台にいる場合にジャンプ可能
        if self.on_box:
            if self.current_box_color == 10: #  黄色の場合
                self.red = 1
                self.vy = 11
            elif self.current_box_color == 8: #  赤の場合
                self.red = 1.5
                self.vy = 9
            elif self.current_box_color == 12: #  青の場合
                self.red = 1
                self.blue = True
                self.vy = 9
                self.last_input_time = pyxel.frame_count
        elif self.blue and (pyxel.frame_count - self.last_input_time) > self.input_cooldown:
            self.red = 1
            self.blue = False
            self.vy = 9
        elif self.y == 214:
            self.red = 1
            self.vy = 9
        self.on_box = False  # ジャンプしたので踏み台から離れた

    def move_left(self):
        self.vx = -5 * self.red

    def move_right(self):
        self.vx = 5 * self.red

    def stop(self):
        self.vx = 0

    def draw(self, current_character):
        if current_character == "monkey":
            pyxel.blt(self.x - 3, self.y - 3, 0, 0, 24, 16, 16, 3)
        elif current_character == "chicken":
            pyxel.blt(self.x - 3, self.y - 3, 0, 16, 24, 16, 16, 3)
        elif current_character == "dog":
            pyxel.blt(self.x - 3, self.y - 3, 0, 32, 24, 16, 16, 3)
        elif current_character == "owl":
            pyxel.blt(self.x - 3, self.y - 3, 0, 48, 24, 16, 16, 3)
        
        
    def _collides_with_box(self, box):
        return (self.x < box.x + box.width and
                self.x + self.width > box.x and
                self.y < box.y + box.height and
                self.y + self.height > box.y)
    
    def _collides_with_obstacle(self, obstacle):
        padding = 2  # 衝突領域を拡大するためのパディング
        return (self.x < obstacle.x + obstacle.width + padding and
                self.x + self.width + padding > obstacle.x and
                self.y < obstacle.y + obstacle.height + padding and
                self.y + self.height + padding > obstacle.y)

    def collides_with_poison(self, poison_height):
        # プレイヤーの位置が毒の位置と重なっているか
        return self.y + self.height > pyxel.height - poison_height