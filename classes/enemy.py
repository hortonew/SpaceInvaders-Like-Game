import physicalobject
import resources
from config import *


class EnemyGroup(object):
    def __init__(self, number_of_enemies, batch):
        self.enemies = []
        self.number_of_enemies = number_of_enemies
        self.left_x_bound = 200
        self.right_x_bound = 800
        self.top_y_bound = 700
        self.bottom_y_bound = 200
        self.x = self.left_x_bound
        self.y = self.top_y_bound

        # make sure that when you generate enemies,
        # you generate them in the correct configuration
        y_offset = self.top_y_bound
        for i in range(0, number_of_enemies):
            next_enemy_x = int(self.left_x_bound)
            while not next_enemy_x >= self.right_x_bound and len(self.enemies) < self.number_of_enemies:
                next_enemy_y = y_offset
                self.enemies.append(Enemy(x=next_enemy_x, y=next_enemy_y, batch=batch))
                next_enemy_x += ENEMY_MARGIN[0]
            y_offset -= int(ENEMY_MARGIN[1])

    def update(self, dt):
        rightmost_enemy_x = max([enemy.x for enemy in self.enemies])
        leftmost_enemy_x = min([enemy.x for enemy in self.enemies])
        if rightmost_enemy_x >= WINDOW_SIZE[0]:
            for enemy in self.enemies:
                enemy.direction = 'left'
                enemy.y -= ENEMY_MARGIN[1]
        elif leftmost_enemy_x <= 0:
            for enemy in self.enemies:
                enemy.direction = 'right'
                enemy.y -= ENEMY_MARGIN[1]
        for enemy in self.enemies:
            enemy.update(dt)


class Enemy(physicalobject.PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Enemy, self).__init__(img=resources.invader1_image, *args, **kwargs)
        self.direction = 'right'

    def update(self, dt):
        super(Enemy, self).update(dt)
        if self.direction is 'right':
            self.x += ENEMY_SPEED
        else:
            self.x -= ENEMY_SPEED