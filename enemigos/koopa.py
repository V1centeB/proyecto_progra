import pyxel
from enemigos.enemigos import Enemigos

class Koopa(Enemigos):

    def draw(self):
        if self.dir == "left":
            pyxel.blt(self.x, self.y, 0, 191, 0, 16, 15)
        elif self.dir == "right":
            pyxel.blt(self.x, self.y, 0, 5, 0, 16, 15)

        
        
        
    def volteado(self):
        if self.golpeado == 3:
            self.stop_moving = True
        if self.golpeado > 3:
            self.stop_moving = False
            self.golpeado = 0
            
    