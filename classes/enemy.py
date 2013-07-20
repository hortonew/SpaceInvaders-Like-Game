import physicalobject
import resources
from pyglet.image import Animation
from pyglet.sprite import Sprite
from gameitem import GameItem
from config import *

class EnemyGroup(GameItem):
    def __init__(self, number_of_enemies, enemy_type, batch):
        GameItem.__init__(self)
        self.enemies = []
        self.number_of_enemies = number_of_enemies
        self.left_x_bound = 200
        self.right_x_bound = 800
        self.top_y_bound = 700
        self.bottom_y_bound = 200
        self.x = self.left_x_bound
        self.y = self.top_y_bound
        self.remove_from_game = False

        # make sure that when you generate enemies,
        # you generate them in the correct configuration
        y_offset = self.top_y_bound
        for i in range(0, number_of_enemies):
            next_enemy_x = int(self.left_x_bound)
            while not next_enemy_x >= self.right_x_bound and len(self.enemies) < self.number_of_enemies:
                next_enemy_y = y_offset
                self.enemies.append(Enemy(resources.enemy_resources[enemy_type], x=next_enemy_x, y=next_enemy_y, batch=batch))
                next_enemy_x += ENEMY_MARGIN[0]
            y_offset -= int(ENEMY_MARGIN[1])


    def remove_enemy(self, e):
        self.enemies.remove(e)
    
    def collides_with(self, _):
        return False

    def update(self, dt):
        for enemy in [enemy for enemy in self.enemies if enemy.remove_from_game is True]:
            self.remove_enemy(enemy)
        if len(self.enemies) > 0:

            rightmost_enemy_x = max([enemy.sprite.x for enemy in self.enemies]) 
            leftmost_enemy_x = min([enemy.sprite.x for enemy in self.enemies]) 
            if rightmost_enemy_x >= WINDOW_SIZE[0] - 40:
                for enemy in self.enemies:
                    enemy.direction = 'left'
                    enemy.sprite.y -= ENEMY_MARGIN[1]
            elif leftmost_enemy_x <= 0:
                for enemy in self.enemies:
                    enemy.direction = 'right'
                    enemy.sprite.y -= ENEMY_MARGIN[1]
        else:
            self.game.remove(self)
            self.game.win_game()


class Enemy(physicalobject.PhysicalObject):
    def __init__(self, seq, *args, **kwargs):
        super(Enemy, self).__init__(Sprite(Animation.from_image_sequence(seq, ENEMY_ANIM_SPEED), *args, **kwargs))
        self.direction = 'right'
        self.game.objects.append(self)

    def update(self, dt):
        #super(Enemy, self).update(dt)
        if self.direction is 'right':
            self.sprite.x += ENEMY_SPEED
        else:
            self.sprite.x -= ENEMY_SPEED

    def clean_up(self):
        self.sprite.delete()
