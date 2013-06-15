import pyglet
from classes import resources, player
from classes.enemy import *
from config import *

game_window = pyglet.window.Window(*WINDOW_SIZE)

main_batch = pyglet.graphics.Batch()

# Initialize the player sprite
player_ship = player.Player(x=400, y=300, batch=main_batch)

#invader1 = Enemy(x=400, y=700, batch=main_batch)
game_objects = [player_ship]
eg = EnemyGenerator(4, main_batch).enemies
for e in eg:
    game_objects.append(e)
# Tell the main window that the player object responds to events
game_window.push_handlers(player_ship.key_handler)


@game_window.event
def on_draw():
	game_window.clear()

	main_batch.draw()


def update(dt):
	for obj in game_objects:
		obj.update(dt)


if __name__ == "__main__":
	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.app.run()