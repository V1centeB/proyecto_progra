import pyxel
import random

class Enemigos:

    def __init__(self, x, y, w, h, dir) -> None:
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.dir = dir
        self.count_fall = -1
        self.count_sprits = 0
        self.count_back_to_live = 0
        self.count_molest = 0
        self.nivel = 3
        self.is_falling = False
        self.num_veces_golpeado = 0
        self.stop_moving = False
        self.speed = 1


    def move_enemigos(self):

        if self.dir == "left" and not self.is_falling and not self.stop_moving:
            self.x -= self.speed
            if self.x <= -14:
                self.x = self.width - 8
        elif self.dir == "left" and self.is_falling:
            self.x -= self.speed

        elif self.dir == "right" and not self.is_falling and not self.stop_moving:
            self.x += self.speed
            if self.x >= self.width:
                self.x = -14  
        elif self.dir == "right" and self.is_falling:
            self.x += self.speed
        self.tuberias()
        self.limitaciones_enemigos()

    def enemigos_fall(self):
        if self.is_falling:
            self.y += (self.count_fall**2) *0.05
            self.count_fall-=1

    def tuberias(self):
        # dentro tuberia
        if (self.x == 26 or self.x + 16 == 218) and self.y == 188 and not self.stop_moving:
            self.y -= 6

        if self.x == 206 and self.y == 182 and not self.stop_moving:
            self.tuberia_dcha = True
            self.x = 34
            self.y = 25
            self.nivel = 3

        if (self.x, self.y) == (-12, 182) and self.dir == "left" and not self.stop_moving:
            self.tuberia_izda = True
            self.x = 190
            self.y = 25
            self.nivel = 3

    def muerte_enemigo(self, mario):
        if (self.x >= mario.x and self.x <= mario.x + 16) and (mario.y <= self.y + 24 or self.y >= mario.y + 22) and mario.nivel == self.nivel - 1:
            self.num_veces_golpeado += 3
        if (mario.x +16 >= self.x and mario.x <= self.x + 16) and mario.nivel == self.nivel and self.stop_moving:
            mario.puntuacion += 800

    def limitaciones_enemigos(self):

        #Caida inicial (caida de la tuberia)
        if (self.x == 34 or self.x == 190) and self.y == self.height - 195:
            self.count_fall = -10
            self.is_falling = True

        if self.y == 51.7: 
            self.y = self.height - 155 - 15

        self.parte_superior_plataformas()
        self.caida_plataformas()

    def parte_superior_plataformas(self):

        #Subir a la parte superior de la primera planta
        if (self.x <= 87 or self.x >= self.width - 97) and self.y == 131.3 :
            self.count = -14            
            self.y = 124
            self.nivel = 1


        #Subir a las partes laterales superiores de la segunda planta
        elif (self.x <= 37 or self.x >= self.width - 53) and self.y == 85.10000000000001: #85.0000
            self.count = -14            
            self.y =  82 
            self.nivel = 2



        #Subir parte central superior de la segunda planta
        if (self.x >= (self.width / 2) - 58 and self.x <= 170) and (self.y == 85.10000000000001 or self.y == 82.0): #85.100,82
            self.count = -14            
            self.y =  78 
            self.nivel = 2


                
        #Subir a la parte superior de la tercera planta
        elif (self.x <= 100 or self.x >= self.width - 110) and self.y == 37.5: 
            self.count = -14      
            self.y = 33 
            self.nivel = 3

    def caida_plataformas(self):

        #Caida enemigos primera planta
        if (self.x > 87 and self.x < 148
            ) and self.y == 141.8 and self.nivel == 1: 
            self.is_falling = True
        if self.y == 182.75: 
            self.is_falling = False
            self.nivel = 0
            self.y = 188 

        #Caida enemigos segunda planta partes laterales
        if (self.x > 36 and self.x < self.width - 53
            ) and self.y == 94.8 and self.nivel == 2: 
            self.is_falling = True
        if self.y == 143.75 and self.nivel == 2: 
            self.is_falling = False
            self.nivel = 1
            self.y = 141.8 

        #Caida enemigos segunda planta plataforma central
        if (self.x < (self.width / 2) - 58 or self.x > 170
            ) and self.y == 93.8 and self.nivel == 2: 
            self.is_falling = True
        if self.y == 134.75 and self.nivel == 2:
            self.is_falling = False
            self.nivel = 1
            self.y = 141.8 

        #Caida enemigos tercera planta
        if (self.x > 100 and self.x < self.width - 110
            ) and self.y == self.height - 170 and self.nivel == 3: 
            self.is_falling = True

        if self.y == 90.95: 
            self.y = 93.8 
            self.nivel = 2