import logging
import resources
from pyglet.image import Animation
from pyglet.sprite import Sprite
from gameitem import GameItem
import physicalobject, bullet
from config import *

logger = logging.getLogger(__name__)

class EnemyGroup(GameItem):
    def __init__(self, number_of_enemies, enemy_type, batch):
        GameItem.__init__(self)
        self.enemies = []
        self.number_of_enemies = number_of_enemies
        self.left_x_bound = 200
        self.right_x_bound = 800
        self.top_y_bound = 650
        self.bottom_y_bound = 200
        self.x = self.left_x_bound
        self.y = self.top_y_bound
        self.remove_from_game = False

        # make sure that when you generate enemies,
        # you generate them in the correct configuration
        y_offset = self.top_y_bound
        row = 0
        for i in range(0, number_of_enemies):
            next_enemy_x = int(self.left_x_bound)
            while not next_enemy_x >= self.right_x_bound and len(self.enemies) < self.number_of_enemies:
                next_enemy_y = y_offset
                self.enemies.append(Enemy(resources.enemy_resources[enemy_type],
                                          row=row,
                                          x=next_enemy_x,
                                          y=next_enemy_y,
                                          batch=batch))
                next_enemy_x += ENEMY_MARGIN[0]
            y_offset -= int(ENEMY_MARGIN[1])
            row += 1

    def reset_position(self):
        logger.info("reset position of EnemyGroup")
        logger.info("self.enemies[0].y {}".format(self.enemies[0].sprite.y))
        diff = self.top_y_bound - self.enemies[0].sprite.y
        for enemy in self.enemies:
            # find the difference between the first enemy's y and the top y bound
            # add that to enemy sprite y
            enemy.sprite.y += diff

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
    def __init__(self, seq, row, *args, **kwargs):
        super(Enemy, self).__init__(sprite=Sprite(Animation.from_image_sequence(seq, ENEMY_ANIM_SPEED), *args, **kwargs))
        self.direction = 'right'
        self.row = row
        self.game.objects.append(self)

    def update(self, dt):
        #super(Enemy, self).update(dt)
        if self.direction is 'right':
            self.sprite.x += ENEMY_SPEED
        else:
            self.sprite.x -= ENEMY_SPEED

    def fire(self):
        logger.info("shot a bullet!")
        bullet_x = self.sprite.x
        bullet_y = self.sprite.y - 20
        b = bullet.Bullet(ENEMY_BULLET_SPEED,
                          bullet_x,
                          bullet_y,
                          batch=self.game.graphics_batch,
                          parent=type(self))
        self.game.objects.append(b)

    def clean_up(self):
        self.sprite.delete()
