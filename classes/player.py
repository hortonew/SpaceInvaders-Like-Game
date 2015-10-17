import logging

from pyglet.window import key
from pyglet.sprite import Sprite
import physicalobject, resources, bullet
from enemy import Enemy
from gameitem import GameItem
from config import PLAYER_THRUST, PLAYER_LIVES, PLAYER_BULLET_SPEED

logger = logging.getLogger(__name__)


class Player(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(Sprite(img=resources.player_image, *args, **kwargs))

        self.lives = PLAYER_LIVES
        self.bullet_speed = PLAYER_BULLET_SPEED
        self.dx = 0

        # Place for key mappings
        self.up = key.W
        self.left = key.A
        self.right = key.D
        self.down = key.S
        self.space = key.SPACE

        self.win.push_handlers(self.on_key_press, self.on_key_release)

    def clean_up(self):
        self.win.remove_handlers(self.on_key_press, self.on_key_release)
        self.sprite.delete()

    def respawn(self):
        self.lives -= 1
        self.x = 400
        self.y = 300
        self.velocity_x, self.velocity_y = 0.0, 0.0
        logger.info("Died once! Lives: {}".format(self.lives))
        self.game.enemy_group.reset_position()
        self.game.lives.update_lives(self.lives)
        if self.lives <= 0:
            logger.info("Game over! Lives: {}".format(self.lives))
            self.game.lose_game()

    def fire(self):
        logger.info("shot a bullet!")
        bullet_x = self.sprite.x
        bullet_y = self.sprite.y + 10
        b = bullet.Bullet(PLAYER_BULLET_SPEED, bullet_x, bullet_y, batch=self.game.graphics_batch)
        self.game.objects.append(b)

    def update(self, dt):
        self.sprite.x += self.dx

        super(Player, self).update(dt)

    def on_key_press(self, k, __):
        if k == self.left:
            self.dx = -10
        if k == self.right:
            self.dx = 10

        if k == self.space:
            self.fire()

    def on_key_release(self, k, __):
        if k == self.left or k == self.right:
            self.dx = 0

    def handle_collision_with(self, other_object):
        if other_object.__class__ == Enemy:
            self.respawn()
