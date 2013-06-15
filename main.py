import pyglet

window = pyglet.window.Window(1024,768)


def update(dt):
	pass


@window.event
def on_draw():
	pass

if __name__ == "__main__":
	pyglet.clock.schedule_interval(update, 1/1)
	pyglet.app.run()