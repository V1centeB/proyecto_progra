import pyxel
import graficos
from mario import Mario
from enemigos.koopa import Koopa
from enemigos.sides import Sides
from enemigos.enemigos import Enemigos


class Tablero:
    """Encontraremos tanto el Update como los draw de todos los assets necesarios"""

    def __init__(self, w, h):
        self.width = w
        self.height = h



    def crear_objetos(self):
        """Creamos todos los objetos que usaremos en el juego"""
        #Creamos Mario
        self.mario = Mario(self.width / 2, self.height - 38, self.width, self.height)
        #Creamos tuberias
        #Tuberias inferires
        self.tuberia0_izq = graficos.Tuberias(0, self.height - 43)
        self.tuberia0_der = graficos.Tuberias(self.width - 26, self.height - 43)
        #Tuberias superioes
        self.tuberia1_izq = graficos.Tuberias(-10, self.height - 195)
        #Creamos los distintos pisos 
        #Priemra planta 
        self.primer_nivel_izq = graficos.Bloques(0, self.height - 63)  
        self.primer_nivel_der = graficos.Bloques(self.width - 8, self.height - 63) 
        #Segunda planta
        self.segundo_nivel_izq = graficos.Bloques(0, self.height - 107)  
        self.segundo_nivel_centro = graficos.Bloques((self.width / 2) - 48, self.height - 111)
        self.segundo_nivel_der = graficos.Bloques(self.width - 8, self.height - 107)  
        #tercera Planta 
        self.tercer_nivel_izq = graficos.Bloques(0, self.height - 155)  
        self.tercer_nivel_der = graficos.Bloques(self.width - 8, self.height - 155)  

        #Enemigos
        self.koopa = Koopa(self.width, self.height - 195, self.width, self.height, "left")
        self.side = Sides(0, self.height - 195, self.width, self.height, "right")


    def update(self):
        print(self.side.golpeado)
        #self.mario.caida_mario()
        self.mario.dir = None

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        """---FUNCIONALIDAD MARIO ----"""

        self.mario.limitaciones_mario()
        self.mario.muerte_mario(self.koopa)


        #Movimiento izquierda

        if pyxel.btn(pyxel.KEY_LEFT):
            self.mario.dir = "left"
            self.mario.move_mario()

        #Movimiento derecha
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.mario.dir = "right"
            self.mario.move_mario()

        #Salto (Eliminamos posibilidad de salto doble)
        if not (self.mario.is_jumping):
            if pyxel.btn(pyxel.KEY_A):
                self.mario.is_jumping=True

        else:
            if self.mario.count >= -14 and self.mario.nivel != "tercero":
                self.mario.mario_jump()

            elif self.mario.count >= -14:
                self.mario.mario_jump_low()

            else:
                self.mario.is_jumping = False
                self.mario.count = 14
                self.colision = False

        if self.mario.is_falling:
            self.mario.is_jumping = False
            if self.mario.count_fall >= -13:
                self.mario.mario_fall()              
            else:
                self.mario.is_falling = False
                self.mario.count_fall = 0

        """---FUNCIONALIDAD ENEMIGOS ----"""
        #for self.enemigo in self.enemigos:
        self.koopa.move_enemigos()
        self.koopa.limitaciones_enemigos()
        self.koopa.volteado()
        self.koopa.muerte_enemigo(self.mario)

        self.side.move_enemigos()
        self.side.limitaciones_enemigos()
        self.side.volteado()
        self.side.muerte_enemigo(self.mario)

        if self.koopa.is_falling:
            if self.koopa.count_fall >= -13:
                self.koopa.enemigos_fall()
            else:
                self.koopa.is_falling = False
                self.koopa.count_fall = 0


        if self.side.is_falling:
            if self.side.count_fall >= -13:
                self.side.enemigos_fall()
            else:
                self.side.is_falling = False
                self.side.count_fall = 0


    def draw(self):
        """Funcion que se encarga de dibujarnos todos los sprits en el tablero"""
        #Color de fondo 

            
        #Dibujamos sprits de Mario:

        #Mario estático
        self.mario.draw()

        #Mario movimiento izquierda animado
        if self.mario.dir == "left":
            if self.mario.count_sprits <= 5:
                self.mario.draw_left()
            else:
                self.mario.draw_left_1()

        #Mario saltando
        if self.mario.is_jumping:
            self.mario.draw_jump()


        #Mario cayendo
        if self.mario.is_falling:
            self.mario.draw_fall()

        #Dibujamos planta 0
        pyxel.blt(0, self.height - 16, 2, 0, 205, 248, 50)

        #Dibujamos las tuberías
        self.tuberia0_izq.draw_tuberia0_izq()
        self.tuberia0_der.draw_tuberia0_der()
        self.tuberia1_izq.draw_tuberia1_izq()

        #Dibujamos el resto de plantas(bloques del suelo)
        self.primer_nivel_izq.draw_primer_nivel_izq()
        self.primer_nivel_der.draw_primer_nivel_der()
        self.segundo_nivel_izq.draw_segundo_nivel_izq()
        self.segundo_nivel_centro.draw_segundo_nivel_centro()
        self.segundo_nivel_der.draw_segundo_nivel_der()
        self.tercer_nivel_izq.draw_tercer_nivel_izq()
        self.tercer_nivel_der.draw_tercer_nivel_der()

        """Dibujamos mapa interactivo"""
        #vidas mario
        if self.mario.vidas >= 1:
            pyxel.blt(50, 20, 1, 4, 2, 8, 7)
        if self.mario.vidas >= 2:
            pyxel.blt(62, 20, 1, 4, 2, 8, 7)
        if self.mario.vidas == 3:
            pyxel.blt(74, 20, 1, 4, 2, 8, 7)

        if not self.koopa.stop_moving:
            self.koopa.draw()

        if self.koopa.stop_moving:
            pyxel.blt(self.koopa.x, self.koopa.y + 7, 1, 2, 155, 10, 9)

        if not self.side.stop_moving:  
            self.side.draw()
        
        if self.side.stop_moving:
            pyxel.blt(self.side.x, self.side.y, 0, 131, 88, 16, 15)

