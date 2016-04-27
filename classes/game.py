import logging
import random
from config import *
from classes import player
from classes.bullet import Bullet
from classes.enemy import EnemyGroup, Enemy
from classes.scenes import MainMenu, WinScreen, LoseScreen
from classes.gameitem import GameItem
from classes.hud import Score, Lives
import pyglet

logger = logging.getLogger(__name__)

class Game(object):

    def __init__(self):
        self.win = GameItem.win = pyglet.window.Window(*WINDOW_SIZE)
        self.graphics_batch = pyglet.graphics.Batch()
        self.objects = []
        self.win.on_draw = self.on_draw
        self.lost_game = False
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
                if type(obj) == Bullet:
                    if self.player.collides_with(obj):
                        self.player.handle_collision_with(obj)
                for enemy in [oo for oo in self.objects if type(oo) == Enemy]:
                    if obj.collides_with(enemy):
                        obj.handle_collision_with(enemy)
                        enemy.handle_collision_with(obj)
                        # wonky score function for that arcade feel
                        self.score.update_score(self.score.score + (MYSTERY_SCORE_NUMBER * (enemy.row + 1)))

            # update all game objects
            obj.update(dt)

        for to_remove in [obj for obj in self.objects if obj.remove_from_game]:
            self.objects.remove(to_remove)
            to_remove.clean_up()
            #del(to_remove)

    def enemy_fire(self, dt):
        # pick random enemy and make it fire
        enemies = [obj for obj in self.objects if type(obj) == Enemy]
        if enemies:
            random_enemy = enemies[random.randint(0, len(enemies) - 1)]
            random_enemy.fire()


    def start(self, _):
        # Initialize the player sprite
        self.player = player.Player(x=WINDOW_SIZE[0]//2, y=100, batch=self.graphics_batch)
        self.lives = Lives(self.player.lives)
        self.score = Score()
        self.enemy_group = EnemyGroup(NUM_ENEMIES, 0, self.graphics_batch)
        self.objects.append(self.player)
        self.objects.append(self.enemy_group)
        self.objects.append(self.score)
        self.objects.append(self.lives)

    def win_game(self):
        if not self.lost_game:
            for o in self.objects:
                pyglet.clock.schedule_once(o.remove, 0)
            self.add(WinScreen())

    def lose_game(self):
        self.lost_game = True
        for o in self.objects:
            pyglet.clock.schedule_once(o.remove, 0)
        self.add(LoseScreen())
    
    def main(self):
        self.add(MainMenu())
        pyglet.clock.schedule_interval(self.update, 1/120.0)
        pyglet.clock.schedule_interval(self.enemy_fire, 3)
        pyglet.app.run()
        # start main menu
