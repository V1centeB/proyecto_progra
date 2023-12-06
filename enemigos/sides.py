import pyxel

from enemigos.enemigos import Enemigos

class Sides(Enemigos):

    def __init__(self, x:int, y:int, w:int, h:int, dir:str) -> None:
        super().__init__(x, y, w, h, dir)

    def draw(self):
        if self.count_sprits <= 5:
            if self.num_veces_golpeado < 3:
                pyxel.blt(self.x, self.y, 0, 31, 90, 16, 15)
            else:
                pyxel.blt(self.x, self.y, 0, 56, 88, 16, 15)
            self.count_sprits += 1
        else:
            if self.num_veces_golpeado < 3:
                pyxel.blt(self.x, self.y, 0, 5, 90, 16, 15)
            else:
                pyxel.blt(self.x, self.y, 0, 82, 88, 16, 15)  
            if self.count_sprits >= 10:
                self.count_sprits = 0
            self.count_sprits += 1


    def volteado(self):
        if self.num_veces_golpeado == 6:
            self.stop_moving = True
        if self.num_veces_golpeado > 6:
            self.stop_moving = False
            self.num_veces_golpeado = 0
            