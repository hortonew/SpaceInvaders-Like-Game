import math
from pyglet.window import key
import physicalobject, resources
from config import *


class EnemyGenerator(object):
    def __init__(self, number_of_enemies, batch):
        self.enemies = []
        for i in range(0, number_of_enemies):
            self.enemies.append(Enemy(x=400 + (i*60), y=700, batch=batch))


class Enemy(physicalobject.PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Enemy, self).__init__(img=resources.invader1_image, *args, **kwargs)
        self.direction = 'right'

    def update(self, dt):
        super(Enemy, self).update(dt)
        if self.direction is 'right':
            self.x += 10
        else:
            self.x -= 10

        if self.x >= WINDOW_SIZE[0]:
            self.direction = 'left'
            self.y -= 40
        elif self.x <= 0:
            self.direction = 'right'
            self.y -= 40
