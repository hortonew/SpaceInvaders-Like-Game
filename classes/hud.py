from config import *
from gameitem import GameItem
import pyglet


class Score(GameItem):
    
    def __init__(self):
        GameItem.__init__(self)
        self.score = 0
        self.label = pyglet.text.Label("score "+"{0:09d}".format(self.score),
                                        font_name='sans-serif',
                                        font_size=26,
                                        x=WINDOW_SIZE[0] - 200,
                                        y=WINDOW_SIZE[1] - 50,
                                        anchor_x='center',
                                        anchor_y='center',
                                        batch=self.game.graphics_batch)

    def update_score(self, new_score):
        # find number of digits, pad with necessary number of zeros
        self.score = new_score
        digits = len(str(new_score))
        self.label.text = "score "+"{0:09d}".format(self.score)
        self.draw()

    def update(self, dt):
        pass


    def draw(self):
        self.label.draw()

    def clean_up(self):
        self.label.delete()
