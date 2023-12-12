import pyxel
from enemigos.enemigos import Enemigos

class Tuberias:
    """Ubicaremos la funcionalidad de las tuberias"""
    def __init__(self, x, y):
          
        self.x = x
        self.y = y

    def draw_tuberia0_izq(self):    
        pyxel.blt(self.x, self.y, 2, 8, 234, 26, 27)

    def draw_tuberia0_der(self):     
        pyxel.blt(self.x, self.y, 2, 7, 170, 26, 27)

    def draw_tuberia1_izq(self):
          pyxel.blt(self.x, self.y, 2, 47, 158, 47, 32)

    def draw_tuberia1_der(self):
          pyxel.blt(self.x, self.y, 2, 49, 222, 47, 32)

class Bloques:
    """Ubicaremos la funcionalidad de los bloques """
    def __init__(self, x, y):
          
          self.x = x
          self.y = y

    def draw_primer_nivel_izq(self):
            pos = 0
            for i in range(11):
                pyxel.blt(self.x + pos, self.y, 2, 108, 186, 7, 7)
                pos += 8

    def draw_primer_nivel_der(self):
            pos = 0
            for i in range(11):
                pyxel.blt(self.x - pos, self.y, 2, 108, 186, 7, 7)
                pos += 8

    def draw_segundo_nivel_izq(self):
            pos = 0
            for i in range(5):
                pyxel.blt(self.x + pos, self.y, 2, 108, 186, 7, 7)
                pos += 8

    def draw_segundo_nivel_centro(self):
            pos = 0
            for i in range(12):
                pyxel.blt(self.x + pos, self.y, 2, 108, 186, 7, 7)
                pos += 8

    def draw_segundo_nivel_der(self):
            pos = 0
            for i in range(5):
                pyxel.blt(self.x - pos, self.y, 2, 108, 186, 7, 7)
                pos += 8

    def draw_tercer_nivel_izq(self):
            pos = 0
            for i in range(13):
                pyxel.blt(self.x + pos, self.y, 2, 108, 186, 7, 7)
                pos += 8

    def draw_tercer_nivel_der(self):
            pos = 0
            for i in range(13):
                pyxel.blt(self.x - pos, self.y, 2, 108, 186, 7, 7)
                pos += 8

class Monedas(Enemigos):
    
    def __init__(self, x:int, y:int, w:int, h:int, dir:str) -> None:
        super().__init__(x, y, w, h, dir)
        
    def draw(self):
        if self.count_sprits <= 5:
            pyxel.blt(self.x, self.y, 2, 165, 50, 7, 11)
        elif self.count_sprits <= 10:
            pyxel.blt(self.x, self.y, 2, 165, 50, 7, 11)
        else:
            pyxel.blt(self.x, self.y, 2, 150, 50, 1,  11)
        self.count_sprits += 1
        if self.count_sprits > 15:
            self.count_sprits = 0

    def move_monedas(self):
        self.movimiento_basico()
        self.parte_superior_plataformas()
        self.caida_plataformas()
        self.entrar_tub()

    def movimiento_basico(self):
        # Caida inicial (caida de la tuberia)
        if (self.x == 34 or self.x == 190) and self.y == self.height - 195:
            self.count_fall = -10
            self.is_falling = True

        if self.y == 51.7:
            self.y = self.height - 155 - 15

        if self.dir == "left" and not self.is_falling and not self.stop_moving:
            self.x -= self.speed
            if self.x <= -14 and not self.nivel == 0:
                self.x = self.width - 8
        elif self.dir == "left" and self.is_falling:
            self.x -= self.speed

        elif self.dir == "right" and not self.is_falling and not self.stop_moving:
            self.x += self.speed
            if self.x >= self.width and not self.nivel == 0:
                self.x = -14
        elif self.dir == "right" and self.is_falling:
            self.x += self.speed
    
    def entrar_tub(self):
        if (self.x == 27 or self.x + 16 == 218) and self.y == 188 and not self.stop_moving and self.dir == "left":
            self.y -= 6
        if self.x + 16 == 218 and self.y == 188 and not self.stop_moving and self.dir =="right":
            self.y -= 6
 

    def colision_mario(self, mario, lista_monedas):
        if (mario.x +16 >= self.x and mario.x <= self.x + 16) and mario.nivel == self.nivel:
            mario.monedas_counter += 1
            self.suma = True
            lista_monedas.remove(self)

            
class Counter:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.suma = False

    def draw(self):
        puntuacion = str(self.value).zfill(6)[-6:]
        pyxel.text(self.x, self.y, "TOP-", 9)
        pyxel.text(self.x+16, self.y, puntuacion, 7)


    def update(self, new_value):
        self.value = new_value

class MonedasCounter:
    def __init__(self, x, y, value_monedas):
        self.x = x
        self.y = y
        self.value_monedas = value_monedas
        self.suma = False

    def draw(self):
        monedas = str(self.value_monedas).zfill(6)[-6:]
        pyxel.text(self.x, self.y, "I-", 11)
        pyxel.text(self.x+9, self.y, monedas, 7)


    def update(self, new_value):
        self.value_monedas = new_value

class Pow:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pyxel.blt(self.x, self.y, 2, 128, 154, 17, 17)
    