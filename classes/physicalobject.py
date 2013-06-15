import pyglet

class PhysicalObject(pyglet.sprite.Sprite):

	def __init__(self, *args, **kwargs):
		super(PhysicalObject, self).__init__(*args, **kwargs)

		self.velocity_x, self.velocity_y = 0.0, 0.0

	def update(self, dt):
		self.x += self.velocity_x * dt
		self.y += self.velocity_y * dt

		self.check_bounds()

	def check_bounds(self):
		min_x = -self.image.width/2
		min_y = -self.image.height/2
		max_x = 1024 + self.image.width/2
		max_y = 768 + self.image.height/2

		#if object moves off screen horizontally, put it on the opposite side of the screen
		if self.x < min_x:
			self.x = max_x
		elif self.x > max_x:
			self.x = min_x

		#if object moves off screen vertically, put it on the opposite side of the screen
		if self.y < min_y:
			self.y = max_y
		elif self.y > max_y:
			self.y = min_y