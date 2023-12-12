import pyxel

from enemigos.enemigos import Enemigos

class Sides(Enemigos):

    def __init__(self, x:int, y:int, w:int, h:int, dir:str) -> None:
        super().__init__(x, y, w, h, dir)

    def draw(self):
        if not self.stop_moving:
            if self.count_molest == 0:
                self.draw_0()
            elif self.count_molest == 1:
                self.draw_1()
            elif self.count_molest == 2:
                self.draw_2()

        elif self.stop_moving:
            if self.count_molest == 0:
                self.draw_s_0()
            elif self.count_molest == 1:
                self.draw_s_1()
            elif self.count_molest == 2:
                self.draw_s_2()


    def draw_0(self):
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

    def draw_1(self):
        if self.count_sprits <= 5:
            if self.num_veces_golpeado < 3:
                pyxel.blt(self.x, self.y, 0, 31, 114, 16, 15)
            else:
                pyxel.blt(self.x, self.y, 0, 56, 111, 16, 15)
            self.count_sprits += 1
        else:
            if self.num_veces_golpeado < 3:
                pyxel.blt(self.x, self.y, 0, 5, 114, 16, 15)
            else:
                pyxel.blt(self.x, self.y, 0, 82, 111, 16, 15)  
            if self.count_sprits >= 10:
                self.count_sprits = 0
            self.count_sprits += 1

    def draw_2(self):
        if self.count_sprits <= 5:
            if self.num_veces_golpeado < 3:
                pyxel.blt(self.x, self.y, 0, 31, 140, 16, 15)
            else:
                pyxel.blt(self.x, self.y, 0, 56, 137, 16, 15)
            self.count_sprits += 1
        else:
            if self.num_veces_golpeado < 3:
                pyxel.blt(self.x, self.y, 0, 5, 140, 16, 15)
            else:
                pyxel.blt(self.x, self.y, 0, 82, 137, 16, 15)  
            if self.count_sprits >= 10:
                self.count_sprits = 0
            self.count_sprits += 1

    def draw_s_0(self):
        pyxel.blt(self.x, self.y, 0, 131, 88, 16, 15)

    def draw_s_1(self):
        pyxel.blt(self.x, self.y, 0, 131, 112, 16, 15)

    def draw_s_2(self):
        pyxel.blt(self.x, self.y, 0, 131, 138, 16, 15)

    def volteado(self):
        if self.num_veces_golpeado == 6 or self.golpear_all == True:
            self.stop_moving = True
            self.count_back_to_live += 1
        if self.num_veces_golpeado > 6 or self.count_back_to_live == 130 and self.golpear_all == True:
            self.stop_moving = False
            self.golpear_all = False
            self.num_veces_golpeado = 0
            self.count_back_to_live = 0
            if self.count_molest < 2:
                self.speed += 0.5
                self.count_molest += 1

    def muerte_enemigo(self, mario, lista_enemigos):
        if (self.x >= mario.x and self.x <= mario.x + 16) and (mario.y <= self.y + 24 or self.y >= mario.y + 22) and mario.nivel == self.nivel - 1:
            self.num_veces_golpeado += 3
            mario.puntuacion += 10
            self.suma = True
        if (mario.x +16 >= self.x and mario.x <= self.x + 16) and mario.nivel == self.nivel and self.stop_moving:
            mario.puntuacion += 800
            self.suma = True
            lista_enemigos.remove(self)
      