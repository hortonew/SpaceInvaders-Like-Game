from classes.menus import MainMenu
from config import *
from classes import player
from classes.enemy import EnemyGroup
from classes.menus import MainMenu
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

    def on_draw(self):
        self.win.clear()
        self.graphics_batch.draw()

    def update(self, dt):
        # update all game objects
        for obj in self.objects:
            obj.update(dt)

        for to_remove in [obj for obj in self.objects if obj.remove_from_game]:
            print to_remove 
            to_remove.clean_up()
            self.objects.remove(to_remove)
            del(to_remove)

    def start(self):
        # Initialize the player sprite
        self.objects.append(player.Player(x=WINDOW_SIZE[0]//2, y=100, batch=self.graphics_batch))
        self.objects.append(EnemyGroup(NUM_ENEMIES, 0, self.graphics_batch))

    
    def main(self):
        self.add(MainMenu(self.graphics_batch))
        pyglet.clock.schedule_interval(self.update, 1/120.0)
        pyglet.app.run()
        # start main menu
