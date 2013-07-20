
class GameItem(object):
    game = None
    win = None

    def __init__(self):
        self.remove_from_game = False


    def remove(self, _):
        self.remove_from_game = True

    def update(self, _):
        pass


