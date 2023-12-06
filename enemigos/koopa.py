import pyxel
from enemigos.enemigos import Enemigos

class Koopa(Enemigos):

    def __init__(self, x:int, y:int, w:int, h:int, dir:str) -> None:
        super().__init__(x, y, w, h, dir)

    def draw(self):
        if self.dir == "left":
            pyxel.blt(self.x, self.y, 0, 191, 0, 16, 15)
        elif self.dir == "right":
            pyxel.blt(self.x, self.y, 0, 5, 0, 16, 15)

        
        
        
    def volteado(self):
        if self.num_veces_golpeado == 3:
            self.stop_moving = True
        if self.num_veces_golpeado > 3:
            self.stop_moving = False
            self.num_veces_golpeado = 0
            
    