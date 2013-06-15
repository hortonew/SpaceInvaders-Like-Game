import math
from pyglet.window import key
import physicalobject, resources

class Player(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
    	super(Player, self).__init__(img=resources.player_image, *args, **kwargs)

        self.thrust = 300.0

        self.keys = dict(left=False, right=False, up=False, down=False)

        #Place to key mappings
        self.up = key.W
        self.left = key.A
        self.right = key.D
        self.down = key.S

        self.key_handler = key.KeyStateHandler()

    def update(self, dt):
		super(Player, self).update(dt)

		if self.key_handler[self.up]:
			force_y = self.thrust * dt
			self.velocity_y += force_y

		if self.key_handler[self.down]:
			force_y = self.thrust * dt
			self.velocity_y -= force_y

		if self.key_handler[self.left]:
			force_x = self.thrust * dt
			self.velocity_x -= force_x

		if self.key_handler[self.right]:
			force_x = self.thrust * dt
			self.velocity_x += force_x