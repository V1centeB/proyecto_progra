import pyxel
from enemigos.enemigos import Enemigos

class Koopa(Enemigos):

    def draw(self):
        if self.dir == "left":
            pyxel.blt(0, self.height - 195, 0, 191, 0, 16, 15)
        elif self.dir == "right":
            pyxel.blt(self.x, self.y, 0, 5, 0, 16, 15)
        