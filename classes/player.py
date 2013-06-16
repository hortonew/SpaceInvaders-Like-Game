from pyglet.window import key
import physicalobject, resources, bullet
from config import PLAYER_THRUST, PLAYER_LIVES, PLAYER_BULLET_SPEED

class Player(physicalobject.PhysicalObject):

	def __init__(self, *args, **kwargs):
		super(Player, self).__init__(img=resources.player_image, *args, **kwargs)

		self.thrust = PLAYER_THRUST
		self.lives = PLAYER_LIVES
		self.bullet_speed = PLAYER_BULLET_SPEED

		self.keys = dict(left=False, right=False, up=False, down=False)

		# Place for key mappings
		self.up = key.W
		self.left = key.A
		self.right = key.D
		self.down = key.S
		self.space = key.SPACE

		self.key_handler = key.KeyStateHandler()

	def delete(self):
		super(Player, self).delete()

	def respawn(self):
		self.lives -= 1
		self.x = 400
		self.y = 300
		self.dead = False
		self.velocity_x, self.velocity_y = 0.0, 0.0

	def fire(self):
		bullet_x = self.x
		bullet_y = self.y + 10
		new_bullet = bullet.Bullet(bullet_x, bullet_y, batch=self.batch)
		bullet_vy = self.bullet_speed
		new_bullet.velocity_y = bullet_vy

		self.new_objects.append(new_bullet)

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

		if self.key_handler[self.space]:
			self.fire()