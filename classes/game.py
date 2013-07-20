from config import *
from classes import player
from classes.bullet import Bullet
from classes.enemy import EnemyGroup, Enemy
from classes.scenes import MainMenu, WinScreen
from classes.gameitem import GameItem
import pyglet


class Game(object):

    def __init__(self):
        self.win = GameItem.win = pyglet.window.Window(*WINDOW_SIZE)
        self.graphics_batch = pyglet.graphics.Batch()
        self.objects = []
        self.win.on_draw = self.on_draw
        GameItem.game = self

    def add(self, new_game_object):
        self.objects.append(new_game_object)

    def remove(self, obj_to_remove):
        self.objects.remove(obj_to_remove) 

    def on_draw(self):
        self.win.clear()
        self.graphics_batch.draw()

    def update(self, dt):
        for obj in self.objects:
            # todo: seriously clean up this hackjob
            if type(obj) in [player.Player, Bullet]:
                for enemy in [oo for oo in self.objects if type(oo) == Enemy]:
                    if obj.collides_with(enemy):
                        obj.handle_collision_with(enemy)
                        enemy.handle_collision_with(obj)
            # update all game objects
            obj.update(dt)

        for to_remove in [obj for obj in self.objects if obj.remove_from_game]:
            self.objects.remove(to_remove)
            to_remove.clean_up()
            #del(to_remove)

    def start(self, _):
        # Initialize the player sprite
        self.player = player.Player(x=WINDOW_SIZE[0]//2, y=100, batch=self.graphics_batch)
        self.objects.append(self.player)
        self.objects.append(EnemyGroup(NUM_ENEMIES, 0, self.graphics_batch))

    def win_game(self):
        pyglet.clock.schedule_once(self.player.remove, 0)
        self.add(WinScreen())
    
    def main(self):
        self.add(MainMenu())
        pyglet.clock.schedule_interval(self.update, 1/120.0)
        pyglet.app.run()
        # start main menu
