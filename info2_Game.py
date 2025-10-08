import pyxel
import random
from info2_Box import Box
from info2_Poison import Poison
from info2_Player import Player
from info2_Obstacle import Obstacle
from info2_Score import Score
class Game:
    def __init__(self, current_character):
        pyxel.load("character.pyxres")
        self.boxes = []#
        self.box = ''#
        self.player = Player()
        self.poison = Poison()
        self.score = Score()#
        self.bottom_color = random.choice((0, 1))#
        self.game_over = False#
        self.gameover_select = 1#
        self.change_to_home = False#
        self.last_input_time = pyxel.frame_count#
        self.box_start = 220#
        self.balls = [Obstacle() for _ in range(2)]  #
        self.player_life = 3
        self.result_score = 0#
        self.show_message = True # 文字を点滅させる
        self.timer = 0#
        self.score_timer = 0#
        self.evaluation = ""#
        self.evaluation_color = 0#
        self.current_character = current_character#

    def update(self):
        if not self.game_over:#
            
            for i in range(4):#
                self.box = Box()
                self.box.create(self.box_start)
                self.boxes.append(self.box)
            self.box_start -= 74
        
            self.player.update(self.boxes)  #
            if pyxel.btn(pyxel.KEY_SPACE) and (pyxel.frame_count - self.last_input_time) > 10: #リスタート時にジャンプ入力が入るのを防ぐため
                self.player.jump()
            if pyxel.btn(pyxel.KEY_LEFT):
                self.player.move_left()
            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.player.move_right()
            else:
                self.player.stop()

            self.poison.update()

            if self.player.collides_with_poison(self.poison.poison_height):
                self.game_over = True
            
            for box in self.boxes:#
                box.scroll()
            
            for ball in self.balls:#
                ball.update()

            if ball.collides_with_player(self.player):
                self.player_life -= 1
                ball.reset()
                if self.player_life <= 0:
                    self.game_over = True
                    return
        else:
            self.timer += 1
            if self.timer >= 20:  
                self.show_message = not self.show_message  # 表示と非表示を切り替える
                self.timer = 0

        for ball in self.balls:
            if not ball.active:
                ball.reset()

    def restart(self):#
        self.boxes = []
        self.box = ''
        self.player = Player()
        self.poison = Poison()
        self.bottom_color = random.choice((0, 1))
        self.background_color =random.choice((3, 4, 5, 6, 7, 9, 11, 13, 14, 15)) 
        self.game_over = False
        self.last_input_time = pyxel.frame_count
        self.box_number = 4
        self.box_start = 220
        self.player_life = 3
        self.score = Score()
        
    
    def draw(self):
        if self.game_over:#
            self.result_score = self.score.score
            self.evaluation = self.score.evaluate(self.result_score)
            self.evaluation_color = self.score.getEvaluationColor(self.evaluation)

            pyxel.cls(13) 

            pyxel.rect(50, 0, 156, 256, 13)
            pyxel.rect(40, 0, 10, 256, 13)
            pyxel.rect(206, 0, 10, 256, 13)
            pyxel.line(39, 0, 39, 256, 0)
            pyxel.line(50, 0, 50, 256, 0)
            pyxel.line(205, 0, 205, 256, 0)
            pyxel.line(216, 0, 216, 256, 0)
            
            pyxel.rect(89, 49, 82, 42, 0)
            pyxel.rect(90, 50, 80, 40, 13)
            pyxel.text(112, 68, "GAME OVER", 0)
            pyxel.rect(89, 103, 82, 20, 0)
            pyxel.rect(90, 104, 80, 18, 7)
            pyxel.text(112, 110, f'Score:{self.result_score}', 0)
            pyxel.text(100, 110, self.evaluation, self.evaluation_color)
            pyxel.rect(89, 128, 82, 20, 0)
            pyxel.rect(90, 129, 80, 18, 13)
            pyxel.text(119, 135, "retry", 0)
            pyxel.rect(89, 153, 82, 20, 0)
            pyxel.rect(90, 154, 80, 18, 13)
            pyxel.text(120, 160, "home", 0)
            
            pyxel.tri(91, 88, 91, 86, 94, 88, 0)
            pyxel.line(91, 84, 96, 88, 0)

            if self.show_message:    
                pyxel.text(87, 190, "press SPACE to select!!", 0)

            if pyxel.btnp(pyxel.KEY_UP) and self.gameover_select == 2:
                self.gameover_select = 1
            elif pyxel.btnp(pyxel.KEY_DOWN) and self.gameover_select == 1:
                self.gameover_select = 2
        
            if self.gameover_select == 1:
                pyxel.tri(72, 135, 72, 141, 78, 138, 0)
            elif self.gameover_select == 2:
                pyxel.tri(72, 160, 72, 166, 78, 163, 0)
            
            if pyxel.btnp(pyxel.KEY_SPACE) and self.gameover_select == 1:
                self.restart()

            if pyxel.btnp(pyxel.KEY_SPACE) and self.gameover_select == 2:
                self.change_to_home = True

        else:
            pyxel.bltm(0, 0, 0, 0, 0, 256, 256, 1)
            pyxel.rect(0, 226, 256, 30, self.bottom_color)
            pyxel.text(40, 240, "SPEED", 8)
            pyxel.text(120, 240, "JUMP", 10)
            pyxel.text(200, 240, "DOUBLE", 12)
        
            for box in self.boxes:#
                box.draw()
            self.player.draw(self.current_character)
            self.poison.draw()
        
            for ball in self.balls:#
                ball.draw()

            if self.player_life == 1:#
                pyxel.blt(5, 5, 0, 48, 8, 8, 8, 3)
            elif self.player_life == 2:
                pyxel.blt(5, 5, 0, 48, 8, 8, 8, 3)
                pyxel.blt(14, 5, 0, 48, 8, 8, 8, 3)
            elif self.player_life == 3:
                pyxel.blt(5, 5, 0, 48, 8, 8, 8, 3)
                pyxel.blt(14, 5, 0, 48, 8, 8, 8, 3)
                pyxel.blt(23, 5, 0, 48, 8, 8, 8, 3)

            self.score_timer += 1
            if self.score_timer >= 2:  
                self.score.updateScore()
                self.score_timer = 0
            pyxel.text(5, 17, f'Score:{self.score.score}', 0)

            
