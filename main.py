import pyxel
import constantes 
from tablero import Tablero
from mario import Mario

#Creamos objetos
tablero = Tablero(constantes.ANCHO,constantes.ALTO)
tablero. crear_objetos()

pyxel.init(tablero.width, tablero.height, "Super Mario Bross")
# Cargamos el fichero pyxres, tiene un gato 16x16 en (0,0) el el banco 0
# Debéis sustituirlo por una imagen de Mario.
#pyxel.load("assets/example.pyxres")
pyxel.load("assets/my_resource.pyxres")
#Cargamos una nave espacial de 16x16 en el banco 1 en (17,0)
#pyxel.image(1).load(17, 0, "assets/player.png")
#Para iniciar el juego, invocamos el método run con las funciones update y draw
pyxel.run(tablero.update, tablero.draw)

