import pyglet
import util
from gameitem import GameItem
from config import SPRITE_SCALE

class PhysicalObject(GameItem):

    def __init__(self, sprite):
        GameItem.__init__(self)
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.scale = SPRITE_SCALE
        self.sprite = sprite
        self.sprite.scale = SPRITE_SCALE
        self.sprite.x = self.sprite.x
        self.sprite.y = self.sprite.y


    def update(self, dt):
        self.sprite.x += self.velocity_x * dt
        self.sprite.y += self.velocity_y * dt

        self.check_bounds()

    def check_bounds(self):
        min_x = -self.sprite.image.width/2
        min_y = -self.sprite.image.height/2
        max_x = 1024 + self.sprite.image.width/2
        max_y = 768 + self.sprite.image.height/2

        #if object moves off screen horizontally, put it on the opposite side of the screen
        if self.sprite.x < min_x:
            self.sprite.x = max_x
        elif self.sprite.x > max_x:
            self.sprite.x = min_x

    def collides_with(self, other_object):
        collision_distance = self.sprite.width/2 + other_object.sprite.width/2
        actual_distance = util.distance(self.sprite.position, other_object.sprite.position)

        return (actual_distance <= collision_distance)

    def handle_collision_with(self, other_object):
        #check if objects are the same type: if not, they die
        if other_object.__class__ == self.__class__:
            self.remove_from_game = False
        else:
            pyglet.clock.schedule_once(self.remove, 0)
