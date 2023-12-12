import pyxel
from enemigos.enemigos import Enemigos

class Mario:
    """Clase con atributos y funciones de Mario"""

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.count = 14
        self.count_fall = -1
        self.count_sprits = 0
        self.width = width
        self.nivel = 0
        self.inmortal = False
        self.vidas = 3
        self.puntuacion = 0
        self.is_jumping = False
        self.is_falling = False
        self.dir = None 
        self.colision = False
        self.mario_dead = False
        self.monedas_counter = 0

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,x):
        self.__x = x


    def draw(self):
        pyxel.cls(0)        
        pyxel.blt(self.x, self.y, 1, 0, 13, 17, 22)

    #Animacion de mario corriendo a izquierdas
    def draw_left(self):
        pyxel.cls(0)
        pyxel.blt(self.x, self.y, 1, 34, 13, 17, 22)
        self.count_sprits += 1

    def draw_left_1(self):
        pyxel.cls(0)
        pyxel.blt(self.x, self.y, 1, 52, 13, 17, 22)
        if self.count_sprits >= 10:
            self.count_sprits = 0  
        self.count_sprits += 1  

    #Animacion de mario saltando 
    def draw_jump(self):
        pyxel.cls(0)
        pyxel.blt(self.x, self.y, 1, 91, 13, 17, 22) 

    #Animacion mario cayendo
    def draw_fall(self):
        pyxel.cls(0)
        pyxel.blt(self.x, self.y, 1, 20, 13, 11, 22) 

    def move_mario(self):
        
        #Movimiento mario direccion izquierda
        if self.dir == "left" and not self.is_falling:
            self.x -= 4
            if self.x <= -14:
                self.x = self.width - 8
        elif self.dir == "left":
            self.x -= 1

        #Movimiento mario direccion derecha 
        elif self.dir == "right" and not self.is_falling:
            self.x += 4
            if self.x >= self.width:
                self.x = -14  
        elif self.dir == "right":
            self.x += 1

    def mario_jump(self):
        if self.count >= -14:
            neg=1
        if self.count<0:
            neg=-1
        self.y -= (self.count**2) *0.05 * neg
        self.count-=1    

    def mario_jump_low(self):
        """Salto con menor altura para evitar que Mario salga del mapa en el tercer nivel"""
        if self.count >= -10:
            neg=1
        if self.count < 0:
            neg =- 1
        self.y -= (self.count**2) *0.05 * neg
        self.count -= 2 

    def mario_fall(self):
        if self.is_falling:
            self.y += (self.count_fall**2) *0.05
            self.count_fall-=1

    def limitaciones_mario(self):
        """Invocamos todas las funciones correspondientes a la movilidad de mario"""
        self.parte_superior_plataformas_mario()
        self.caida_plataformas_mario()
        self.colisiones_mario_plataformas()
        self.vuelta_al_juego()

    def parte_superior_plataformas_mario(self):
        """Permite a Mario caminar sobre plataformas"""
        #Subir a la parte superior de la primera planta
        if (self.x <= 87 or self.x >= self.width - 97) and self.y == 131.3 and not self.is_falling and not self.mario_dead:
            self.count = -14            
            self.y = 126
            self.nivel = 1

        #Subir a las partes laterales superiores de la segunda planta
        if (self.x <= 37 or self.x >= self.width - 53) and self.y == 85.10000000000001 and not self.mario_dead:
            self.count = -14            
            self.y =  82
            self.nivel = 2
            
        #Subir parte central superior de la segunda planta
        if (self.x >= (self.width / 2) - 58 and self.x <= 170) and (self.y == 85.10000000000001 or self.y == 82.0) and not self.mario_dead:
            self.count = -14            
            self.y =  78
            self.nivel = 2

        #Subir a la parte superior de la tercera planta
        if (self.x <= 100 or self.x >= self.width - 110) and self.y == 37.05 and not self.mario_dead:
            self.count = -14      
            self.y = 33
            self.nivel = 3

    def caida_plataformas_mario(self):
        """Permite a Mario bajar de las plataformas"""
        #Caida Mario primera planta
        if (self.x > 87 and self.x < 148
            ) and self.y == 135.8 and self.nivel == 1 and not self.mario_dead:
            self.is_falling = True
        if self.y == 176.75:
            self.is_falling = False
            self.nivel = 0
            self.y = 182

        #Caida Mario segunda planta partes laterales
        if (self.x > 36 and self.x < self.width - 53
            ) and self.y == 91.8 and self.nivel == 2 and not self.mario_dead:
            self.is_falling = True
        if self.y == 132.75 and self.nivel == 2 and not self.mario_dead:
            self.is_falling = False
            self.nivel = 1
            self.y = 135.8
        
        #Caida Mario segunda planta plataforma central
        if (self.x < (self.width / 2) - 58 or self.x > 170
            ) and self.y == 87.8 and self.nivel == 2 and not self.is_jumping and not self.mario_dead:
            self.is_falling = True
        if self.y == 128.75 and self.nivel == 2 and not self.mario_dead:
            self.is_falling = False
            self.nivel = 1
            self.y = 135.8

        #Caida Mario tercera planta
        if (self.x > 100 and self.x < self.width - 110
            ) and self.y == 42.8 and self.nivel == 3 and not self.is_jumping and not self.mario_dead:
            self.is_falling = True
        if self.y == 83.75:
            self.nivel = 2
            self.y = 87.8

        if (self.x >= 100 and self.x <= self.width - 110) and self.nivel == 3 and not self.mario_dead:
            if self.is_jumping and self.y == 42.8:
                self.count = -1
        if self.y == 65.55:
            self.y = 87.8
            self.nivel = 2

    def colisiones_mario_plataformas(self):
        """No permite a Mario atravesar las plataformas"""
        #Colision primera planta
        if (self.x <= 86 or self.x >= self.width - 96) and self.y == 163.75 and not self.mario_dead:
            self.count = -13

        #Colision segunda planta plataformas laterales
        if (self.x <= 36 or self.x >= self.width - 52) and self.y == 117.55000000000001 and not self.mario_dead:
            self.count = -13

        #Colision segunda planta plataforma central
        if (self.x >= (self.width / 2) - 58 and self.x <= 170) and self.y == 110.35000000000001 and not self.mario_dead:
            self.count = -12
            if (self.x > 78 and self.x < self.width - 94):
                self.count = -1
                self.nivel = 0
        elif self.y == 161.10000000000002 and self.nivel == 0 and not self.mario_dead:
            self.y = 182

        #Colision tercera planta 
        if (self.x <= 100 or self.x >= self.width - 110) and (self.y == 66.35 or self.y == 69.55) and not self.mario_dead:
            if self. y == 69.55:
                self.count = -13
            else:
                self.count = -12
            if (self.x > 24 and self.x < 68):
                self.count = -1
                self.nivel = 1

        elif (self.y == 117.1 or self.y == 120.3) and self.nivel != 2 and not self.mario_dead:
            self.y = 135.8

    def colision_pow(self, lista_enemigos, pow):
        if (self.x >= 104 and self.x <= 132) and self.y == 150.5 and self.is_jumping and not self.mario_dead:
            self.count -= 10
            pow.golpes += 1
            for enemigo in lista_enemigos:
                enemigo.golpear_all = True
                
            #faltan las colisiones por los lados y por arriba del pow

    def muerte_mario(self, lista_enemigos):
        for enemigo in lista_enemigos:
            if (self.x >= enemigo.x and self.x <= enemigo.x + 16) and enemigo.nivel == self.nivel and not enemigo.stop_moving and not self.is_jumping:
                if not self.inmortal:
                    self.vidas -= 1
                    self.reaparecer_mario()

    def reaparecer_mario(self):
        self.inmortal = True
        self.x = (self.width / 2) - 13
        self.y = 10
        self.nivel = 3

    def vuelta_al_juego(self):
        if self.inmortal and self.x != (self.width / 2) - 13:
            self.is_falling = True
            self.inmortal = False
        if (self.x > 100 and self.x < self.width - 110):
                if self.y == 50.95:
                    self.is_falling = True
        if self.y == 91.9:
            self.y = 87.8
            self.nivel = 2
