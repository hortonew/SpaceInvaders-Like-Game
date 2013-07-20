from pyglet.window import key
from pyglet.sprite import Sprite
import physicalobject, resources, bullet
from gameitem import GameItem
from config import PLAYER_THRUST, PLAYER_LIVES, PLAYER_BULLET_SPEED

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

    def remove(self):
        #todo: call gameitem's remove
        self.win.remove_handlers(self.on_key_press, self.on_key_release)

    def respawn(self):
        self.lives -= 1
        self.x = 400
        self.y = 300
        self.velocity_x, self.velocity_y = 0.0, 0.0

    def fire(self):
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
