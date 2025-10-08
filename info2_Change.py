import pyxel

class Change:
    def __init__(self, current_character):
        pyxel.load("character.pyxres")
        self.show_message = True # 文字を点滅させる
        self.timer = 0
        self.change_to_home = False
        if current_character == "monkey":
            self.change_select = 1
        elif current_character == "chicken":
            self.change_select = 2
        elif current_character == "dog":
            self.change_select = 3
        elif current_character == "owl":
            self.change_select = 4
        self.current_character = ""
        
    def update(self):
        self.timer += 1

        if self.timer >= 20:  
            self.show_message = not self.show_message  # 表示と非表示を切り替える
            self.timer = 0

        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.change_select == 1:
                self.current_character = "monkey"
            elif self.change_select == 2:
                self.current_character = "chicken"
            elif self.change_select == 3:
                self.current_character = "dog"
            elif self.change_select == 4:
                self.current_character = "owl"
            self.change_to_home = True

    def draw(self):
        pyxel.cls(1)
        
        if self.show_message:    
            pyxel.text(87, 210, "press SPACE to select!!", 7)
        
        if self.change_select == 1:
            pyxel.circ(81, 71, 37, 0)
            pyxel.circ(81, 71, 35, 8)
            pyxel.text(72, 86,"MONKEY",10)
            pyxel.text(160, 86,"CHICKEN",7)
            pyxel.text(77,173,"DOG",7)
            pyxel.text(169, 173,"OWL",7)
        elif self.change_select == 2:
            pyxel.circ(173, 71, 37, 0)
            pyxel.circ(173, 71, 35, 8)
            pyxel.text(72, 86,"MONKEY",7)
            pyxel.text(160, 86,"CHICKEN",10)
            pyxel.text(77,173,"DOG",7)
            pyxel.text(169, 173,"OWL",7)
        elif self.change_select == 3:
            pyxel.circ(81, 158, 37, 0)
            pyxel.circ(81, 158, 35, 8)
            pyxel.text(72, 86,"MONKEY",7)
            pyxel.text(160, 86,"CHICKEN",7)
            pyxel.text(77,173,"DOG",10)
            pyxel.text(169, 173,"OWL",7)
        elif self.change_select == 4:
            pyxel.circ(173, 158, 37, 0)
            pyxel.circ(173, 158, 35, 8)
            pyxel.text(72, 86,"MONKEY",7)
            pyxel.text(160, 86,"CHICKEN",7)
            pyxel.text(77,173,"DOG",7)
            pyxel.text(169, 173,"OWL", 10)
        
        pyxel.blt(74, 64, 0, 0, 24, 16, 16, 3)
        pyxel.blt(166, 64, 0, 16, 24, 16, 16, 3)
        pyxel.blt(74, 151, 0, 32, 24, 16, 16, 3)
        pyxel.blt(166, 151, 0, 48, 24, 16, 16, 3)

        if pyxel.btnp(pyxel.KEY_RIGHT):
            if self.change_select == 1:
                self.change_select = 2
            elif self.change_select == 3:
                self.change_select =4
        elif pyxel.btnp(pyxel.KEY_LEFT):
            if self.change_select == 2:
                self.change_select = 1
            if self.change_select == 4:
                self.change_select =3
        elif pyxel.btnp(pyxel.KEY_UP):
            if self.change_select == 3:
                self.change_select = 1
            if self.change_select == 4:
                self.change_select = 2
        elif pyxel.btnp(pyxel.KEY_DOWN):
            if self.change_select == 1:
                self.change_select = 3
            if self.change_select == 2:
                self.change_select = 4

        
            
            