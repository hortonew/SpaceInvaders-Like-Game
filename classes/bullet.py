import pyglet
import physicalobject, resources
from config import PLAYER_BULLET_SPEED

class Bullet(physicalobject.PhysicalObject):
	def __init__(self, dy, *args, **kwargs):
		super(Bullet, self).__init__(resources.bullet_image, *args, **kwargs)

		#bullets should die after a certain amount of time
		pyglet.clock.schedule_once(self.die, 0.5)
		self.velocity_y = dy 

	def die(self, dt):
		self.dead = True
