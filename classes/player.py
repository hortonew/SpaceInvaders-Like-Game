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

    def on_key_press(self, symbol, modifiers):    
        if symbol == self.up:
            self.keys['up'] = True
        elif symbol == self.left:
            self.keys['left'] = True
        elif symbol == self.right:
            self.keys['right'] = True
        elif symbol == self.down:
        	self.keys['down'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == self.up:
            self.keys['up'] = False
        elif symbol == self.left:
            self.keys['left'] = False
        elif symbol == self.right:
            self.keys['right'] = False
        elif symbol == self.down:
        	self.keys['down'] = False

    def update(self, dt):
		super(Player, self).update(dt)

		if self.keys['up']:
			force_y = self.thrust * dt
			self.velocity_y += force_y

		if self.keys['down']:
			force_y = self.thrust * dt
			self.velocity_y -= force_y

		if self.keys['left']:
			force_x = self.thrust * dt
			self.velocity_x -= force_x

		if self.keys['right']:
			force_x = self.thrust * dt
			self.velocity_x += force_x