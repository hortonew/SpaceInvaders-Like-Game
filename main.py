import pyglet
from classes import player
from classes.enemy import *

game_window = pyglet.window.Window(*WINDOW_SIZE)

main_batch = pyglet.graphics.Batch()

# Initialize the player sprite
player_ship = player.Player(x=400, y=300, batch=main_batch)

#eg = EnemyGroup(NUM_ENEMIES, main_batch)
en1 = Enemy(x=500, y=700, batch=main_batch)
game_objects = [player_ship, en1]


# Tell the main window that the player object responds to events
game_window.push_handlers(player_ship.key_handler)


@game_window.event
def on_draw():
	game_window.clear()

	main_batch.draw()


def update(dt):
	# collision detection
	for i in xrange(len(game_objects)):
		for j in xrange(i+1, len(game_objects)):
			obj_1 = game_objects[i]
			obj_2 = game_objects[j]

			if not obj_1.dead and not obj_2.dead:
				if obj_1.collides_with(obj_2):
					obj_1.handle_collision_with(obj_2)
					obj_2.handle_collision_with(obj_1)

	# update all game objects
	for obj in game_objects:
		obj.update(dt)

	# remove objects from game_objects and delete them
	for to_remove in [obj for obj in game_objects if obj.dead]:
		to_remove.delete()
		game_objects.remove(to_remove)

if __name__ == "__main__":
	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.app.run()