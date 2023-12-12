import pyxel
from enemigos.enemigos import Enemigos


class Koopa(Enemigos):

    def __init__(self, x: int, y: int, w: int, h: int, dir: str) -> None:
        super().__init__(x, y, w, h, dir)
