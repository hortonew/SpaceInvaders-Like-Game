import pyglet
from classes import resources, player

game_window = pyglet.window.Window(1024,768)

main_batch = pyglet.graphics.Batch()

# Initialize the player sprite
player_ship = player.Player(x=400, y=300, batch=main_batch)

invader1 = pyglet.sprite.Sprite(img=resources.invader1_image, x=400, y=700, batch=main_batch)

game_objects = []
game_objects.append(player_ship)

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