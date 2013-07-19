import pyglet
from classes import player
from classes.enemy import *

game_window = pyglet.window.Window(*WINDOW_SIZE)

main_batch = pyglet.graphics.Batch()

# Initialize the player sprite
player_ship = player.Player(x=400, y=300, batch=main_batch)

eg = EnemyGroup(NUM_ENEMIES, 0, main_batch)
game_objects = [player_ship, eg]

# Tell the main window that the player object responds to events
game_window.push_handlers(player_ship.key_handler)


@game_window.event
def on_draw():
	game_window.clear()
	main_batch.draw()


def update(dt):
	# update all game objects
	for obj in game_objects:
		obj.update(dt)
		game_objects.extend(obj.new_objects)
		obj.new_objects = []

	for to_remove in [obj for obj in game_objects if obj.dead]:
		to_remove.delete()
		game_objects.remove(to_remove)
	

if __name__ == "__main__":
	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.app.run()
