import pyxel

from enemigos.enemigos import Enemigos

class Sides(Enemigos):

    def draw(self):
        if self.count_sprits <= 5:
            if self.golpeado < 3:
                pyxel.blt(self.x, self.y, 0, 31, 90, 16, 15)
            else:
                pyxel.blt(self.x, self.y, 0, 56, 88, 16, 15)
            self.count_sprits += 1
        else:
            if self.golpeado < 3:
                pyxel.blt(self.x, self.y, 0, 5, 90, 16, 15)
            else:
                pyxel.blt(self.x, self.y, 0, 82, 88, 16, 15)  
            if self.count_sprits >= 10:
                self.count_sprits = 0
            self.count_sprits += 1


    def volteado(self):
        if self.golpeado == 6:
            self.stop_moving = True
        if self.golpeado > 6:
            self.stop_moving = False
            self.golpeado = 0
            