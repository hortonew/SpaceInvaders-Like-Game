from config import *
from gameitem import GameItem
import pyglet

class MainMenu(GameItem):

    def __init__(self):
        GameItem.__init__(self)
        self.labels = []
        self.labels.append(pyglet.text.Label('SPACE INVADERS-LIKE GAME!',
                                        font_name='sans-serif',
                                        font_size=36,
                                        x=WINDOW_SIZE[0]//2,
                                        y=WINDOW_SIZE[1]//2,
                                        anchor_x='center',
                                        anchor_y='center',
                                        batch=self.game.graphics_batch))

        self.labels.append(pyglet.text.Label('press any key',
                                        font_name='sans-serif',
                                        font_size=26,
                                        x=WINDOW_SIZE[0]//2,
                                        y=WINDOW_SIZE[1]//2 - 100,
                                        anchor_x='center',
                                        anchor_y='center',
                                        batch=self.game.graphics_batch))
        self.win.push_handlers(self.on_key_press)

    def clean_up(self):
        for label in self.labels:
            label.delete()
        self.labels = []
        self.win.remove_handlers(self.on_key_press)


    def update(self, dt):
        pass

    def on_key_press(self, e, __):
        pyglet.clock.schedule_once(self.game.start, 0)
        pyglet.clock.schedule_once(self.remove, 0)


class WinScreen(GameItem):

    def __init__(self):
        GameItem.__init__(self)
        self.new_objects = []
        self.labels = []
        self.labels.append(pyglet.text.Label('YOU WON',
                                        font_name='sans-serif',
                                        font_size=36,
                                        x=WINDOW_SIZE[0]//2,
                                        y=WINDOW_SIZE[1]//2,
                                        anchor_x='center',
                                        anchor_y='center',
                                        batch=self.game.graphics_batch))

        self.labels.append(pyglet.text.Label('press any key',
                                        font_name='sans-serif',
                                        font_size=26,
                                        x=WINDOW_SIZE[0]//2,
                                        y=WINDOW_SIZE[1]//2 - 100,
                                        anchor_x='center',
                                        anchor_y='center',
                                        batch=self.game.graphics_batch))
        self.win.push_handlers(self.on_key_press)

    def clean_up(self):
        for label in self.labels:
            label.delete()
        self.labels = []
        self.win.remove_handlers(self.on_key_press)


    def update(self, dt):
        pass

    def on_key_press(self, e, __):
        pyglet.clock.schedule_once(self.game.start, 0)
        pyglet.clock.schedule_once(self.remove, 0)


class LoseScreen(GameItem):

    def __init__(self):
        GameItem.__init__(self)
        self.new_objects = []
        self.labels = []
        self.labels.append(pyglet.text.Label('YOU LOST!',
                                        font_name='sans-serif',
                                        font_size=36,
                                        x=WINDOW_SIZE[0]//2,
                                        y=WINDOW_SIZE[1]//2,
                                        anchor_x='center',
                                        anchor_y='center',
                                        batch=self.game.graphics_batch))

        self.labels.append(pyglet.text.Label('press any key to play again',
                                        font_name='sans-serif',
                                        font_size=26,
                                        x=WINDOW_SIZE[0]//2,
                                        y=WINDOW_SIZE[1]//2 - 100,
                                        anchor_x='center',
                                        anchor_y='center',
                                        batch=self.game.graphics_batch))
        self.win.push_handlers(self.on_key_press)

    def clean_up(self):
        for label in self.labels:
            label.delete()
        self.labels = []
        self.win.remove_handlers(self.on_key_press)


    def update(self, dt):
        pass

    def on_key_press(self, e, __):
        pyglet.clock.schedule_once(self.game.start, 0)
        pyglet.clock.schedule_once(self.remove, 0)


