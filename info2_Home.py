import pyxel

class Home:
    def __init__(self, current_character):
        pyxel.load("character.pyxres")
        self.show_message = True # 文字を点滅させる
        self.timer = 0
        self.home_select = 1
        self.change_to_game = False
        self.change_to_change = False
        self.current_character = current_character

    def update(self):

        self.timer += 1

        if self.timer >= 20:  
            self.show_message = not self.show_message  # 表示と非表示を切り替える
            self.timer = 0

        if self.home_select == 1 and pyxel.btnp(pyxel.KEY_SPACE):
            self.change_to_game = True

        if self.home_select == 2 and pyxel.btnp(pyxel.KEY_SPACE):
            self.change_to_change = True

    def draw(self):
        pyxel.cls(1) 
        pyxel.rect(50, 0, 156, 256, 8)
        pyxel.rect(40, 0, 10, 256, 10)
        pyxel.rect(206, 0, 10, 256, 10)
        pyxel.line(39, 0, 39, 256, 0)
        pyxel.line(50, 0, 50, 256, 0)
        pyxel.line(205, 0, 205, 256, 0)
        pyxel.line(216, 0, 216, 256, 0)

        pyxel.rect(89, 49, 82, 42, 0)
        pyxel.rect(90, 50, 80, 40, 9)
        pyxel.text(100, 68, "HIGH JUMP QUEST", 7)
        
        pyxel.rect(89, 113, 82, 20, 0)
        pyxel.rect(90, 114, 80, 18, 1)
        pyxel.text(122, 120, "play", 7)
        pyxel.rect(89, 138, 82, 20, 0)
        pyxel.rect(90, 139, 80, 18, 1)
        pyxel.text(118, 145, "change", 7)

        pyxel.tri(91, 88, 91, 86, 94, 88, 0)
        pyxel.line(91, 84, 96, 88, 0)

        if self.current_character == "monkey":
            pyxel.blt(168, 62, 0, 0, 24, 16, 16, 3)
        elif self.current_character == "chicken":
            pyxel.blt(95, 33, 0, 16, 24, 16, 16, 3)
        elif self.current_character == "dog":
            pyxel.blt(105, 97, 0, 32, 24, 16, 16, 3)
        elif self.current_character == "owl":
            pyxel.blt(225, 25, 0, 48, 24, 16, 16, 3)
            pyxel.rect(220, 41, 36, 3, 4)

        if self.show_message:    
            pyxel.text(87, 175, "press SPACE to select!!", 7)

        if pyxel.btnp(pyxel.KEY_DOWN):
            self.home_select = 2
        elif pyxel.btnp(pyxel.KEY_UP):
            self.home_select = 1

        if self.home_select == 1:
            pyxel.tri(72, 120, 72, 126, 78, 123, 0)
        elif self.home_select == 2:
            pyxel.tri(72, 145, 72, 151, 78, 148, 0)


