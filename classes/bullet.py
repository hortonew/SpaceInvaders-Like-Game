import pyglet
import physicalobject, resources

class Bullet(physicalobject.PhysicalObject):
	def __init__(self, *args, **kwargs):
		super(Bullet, self).__init__(resources.bullet_image, *args, **kwargs)

		#bullets should die after a certain amount of time
		pyglet.clock.schedule_once(self.die, 0.5)

	def die(self, dt):
		self.dead = True