import pyxel
import graficos
import random
from mario import Mario
from enemigos.koopa import Koopa
from enemigos.sides import Sides


class Tablero:
    """Encontraremos tanto el Update como los draw de todos los assets necesarios"""

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.lista_enemigos = []
        self.lvl = 0
        self.creo_enemigos = False
        self.contador_crear_enemigos = 10
        self.contador_enemigos_creados = 0
        self.lvl_iniciado = False

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,w):
        self.__width = w

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,height):
        self.__height = height

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
        self.tuberia1_der = graficos.Tuberias(self.width - 38, self.height - 195)
        #Creamos los distintos pisos 
        #Priemra planta 
        self.primer_nivel_izq = graficos.Bloques(0, self.height - 63, self.lvl)  
        self.primer_nivel_der = graficos.Bloques(self.width - 8, self.height - 63, self.lvl) 
        #Segunda planta
        self.segundo_nivel_izq = graficos.Bloques(0, self.height - 107, self.lvl)  
        self.segundo_nivel_centro = graficos.Bloques((self.width / 2) - 48, self.height - 111, self.lvl)
        self.segundo_nivel_der = graficos.Bloques(self.width - 8, self.height - 107, self.lvl)  
        #tercera Planta 
        self.tercer_nivel_izq = graficos.Bloques(0, self.height - 155, self.lvl)  
        self.tercer_nivel_der = graficos.Bloques(self.width - 8, self.height - 155, self.lvl)  

        #Enemigos
        self.koopa = Koopa(0, self.height - 195, self.width, self.height, "right")
        self.side = Sides(self.width, self.height - 195, self.width, self.height, "left")
        self.lista_monedas = []

        # counter
        self.counter = graficos.Counter(85, 10, self.mario.puntuacion)
        self.monedas_counter = graficos.MonedasCounter(45, 10, self.mario.monedas_counter)
        # pow
        self.pow = graficos.Pow(117, self.height-80)


    def crear_monedas(self):
        crear = random.randint(0, 350)
        dir = random.randint(0,1)
        if crear == 50 and dir == 1:
            self.lista_monedas.append(graficos.Monedas(0, self.height - 195, self.width, self.height, "right"))
        elif crear == 50 and dir == 0:
            self.lista_monedas.append(graficos.Monedas(self.width, self.height - 195, self.width, self.height, "left"))

    def crear_enemigos(self):

        if self.contador_crear_enemigos == random.randint(0, 50):
            self.creo_enemigos = True

        if self.lvl == 0 and self.contador_enemigos_creados < 3:
            if self.creo_enemigos:
                self.crear_enemigos_lvl_0()
                self.contador_enemigos_creados += 1
                self.lvl_iniciado = True
        elif self.lvl == 1 and self.contador_enemigos_creados < 7:
            if self.creo_enemigos:
                self.crear_enemigos_lvl_1()
                self.contador_enemigos_creados += 1
                self.lvl_iniciado = True    
        elif self.lvl == 2 and self.contador_enemigos_creados < 10:
            if self.creo_enemigos:
                self.crear_enemigos_lvl_2()
                self.contador_enemigos_creados += 1
                self.lvl_iniciado = True
        elif self.lvl == 3 and self.contador_enemigos_creados < 14:
            if self.creo_enemigos:
                self.crear_enemigos_lvl_3()
                self.contador_enemigos_creados += 1
                self.lvl_iniciado = True     
             
    def crear_enemigos_lvl_0(self):
        directions = ["left", "right"]
        dir = directions[random.randint(0, 1)]
        if dir == "left":
            x = self.width
        else: 
            x = 0
        self.lista_enemigos.append(Koopa(x, self.height - 195, self.width, self.height, dir)) 

    def crear_enemigos_lvl_1(self):
        directions = ["left", "right"]
        dir = directions[random.randint(0, 1)]
        type_enemy = random.randint(0, 1)
        if dir == "left":
            x = self.width
        else: 
            x = 0
        if type_enemy == 0:
            self.lista_enemigos.append(Koopa(x, self.height - 195, self.width, self.height, dir))
        else:
            self.lista_enemigos.append(Sides(x, self.height - 195, self.width, self.height, dir))

    def crear_enemigos_lvl_2(self):
        directions = ["left", "right"]
        dir = directions[random.randint(0, 1)]
        type_enemy = random.randint(0, 1)
        if dir == "left":
            x = self.width
        else: 
            x = 0
        if type_enemy == 0:
            self.lista_enemigos.append(Koopa(x, self.height - 195, self.width, self.height, dir))
        else:
            self.lista_enemigos.append(Sides(x, self.height - 195, self.width, self.height, dir))

    def crear_enemigos_lvl_3(self):
        directions = ["left", "right"]
        dir = directions[random.randint(0, 1)]
        type_enemy = random.randint(0, 1)
        if dir == "left":
            x = self.width
        else: 
            x = 0
        if type_enemy == 0:
            self.lista_enemigos.append(Koopa(x, self.height - 195, self.width, self.height, dir))
        else:
            self.lista_enemigos.append(Sides(x, self.height - 195, self.width, self.height, dir))

    def cambiar_lvl(self):
        if len(self.lista_enemigos) == 0 and self.lvl_iniciado:
            self.lvl += 1
            self.lvl_iniciado = False
            self.contador_enemigos_creados = 0

    def update(self):            
        self.crear_enemigos()
        self.crear_monedas()
        self.cambiar_lvl()
        #self.mario.caida_mario()
        self.mario.dir = None
        self.creo_enemigos = False

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        """---FUNCIONALIDAD MARIO ----"""

        self.mario.limitaciones_mario()
        self.mario.muerte_mario(self.lista_enemigos)
        self.counter.update(self.mario.puntuacion)
        self.monedas_counter.update(self.mario.monedas_counter)
        self.mario.colision_pow(self.lista_enemigos, self.pow)
        self.mario.mario_muere()

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
            if self.mario.count >= -14 and self.mario.nivel != 3:
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
        
        for enemigo in self.lista_enemigos:
            enemigo.move_enemigos()
            enemigo.volteado()
            enemigo.muerte_enemigo(self.mario, self.lista_enemigos)

            if enemigo.is_falling:
                if enemigo.count_fall >= -13:
                    enemigo.enemigos_fall()
                else:
                    enemigo.is_falling = False
                    enemigo.count_fall = 0

        for monedas in self.lista_monedas:
            monedas.move_monedas()
            monedas.colision_mario(self.mario, self.lista_monedas)
            if monedas.is_falling:
                if monedas.count_fall >= -13:
                    monedas.enemigos_fall()
                else:
                    monedas.is_falling = False
                    monedas.count_fall = 0

        if self.pow.golpes > 2:
            for enemigos in self.lista_enemigos:
                enemigos.stop_moving = False
                enemigos.golpear_all = False
            self.pow.golpes = -1

        self.draw_map()


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
        self.tuberia1_der.draw_tuberia1_der()

        #Dibujamos el resto de plantas(bloques del suelo)


        #Dibujamos monedas

        """Dibujamos mapa interactivo"""
        #vidas mario
        if self.mario.vidas >= 1:
            pyxel.blt(50, 20, 1, 4, 2, 8, 7)
        if self.mario.vidas >= 2:
            pyxel.blt(62, 20, 1, 4, 2, 8, 7)
        if self.mario.vidas == 3:
            pyxel.blt(74, 20, 1, 4, 2, 8, 7)

        for enemigo in self.lista_enemigos:
            enemigo.draw()

        for moneda in self.lista_monedas:
            moneda.draw()

        #Draw counter
        self.counter.draw()
        self.monedas_counter.draw()
        #Draw pow
        self.pow.draw()
        self.draw_map()


    def draw_map(self):
        if self.lvl == 0 or self.lvl ==1:
            self.primer_nivel_izq.draw_primer_nivel_izq_1()
            self.primer_nivel_der.draw_primer_nivel_der_1()
            self.segundo_nivel_izq.draw_segundo_nivel_izq_1()
            self.segundo_nivel_centro.draw_segundo_nivel_centro_1()
            self.segundo_nivel_der.draw_segundo_nivel_der_1()
            self.tercer_nivel_izq.draw_tercer_nivel_izq_1()
            self.tercer_nivel_der.draw_tercer_nivel_der_1()

        elif self.lvl == 2 or self.lvl ==3:
            self.primer_nivel_izq.draw_primer_nivel_izq_2()
            self.primer_nivel_der.draw_primer_nivel_der_2()
            self.segundo_nivel_izq.draw_segundo_nivel_izq_2()
            self.segundo_nivel_centro.draw_segundo_nivel_centro_2()
            self.segundo_nivel_der.draw_segundo_nivel_der_2()
            self.tercer_nivel_izq.draw_tercer_nivel_izq_2()
            self.tercer_nivel_der.draw_tercer_nivel_der_2()

    def reiniciar_cont_enemigos(self):

        self.contador_enemigos_creados = 0