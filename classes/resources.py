import pyglet

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

pyglet.resource.path = ['resources/images/']
pyglet.resource.reindex()

#player_image = pyglet.resource.image("ship.png")
player_image = pyglet.resource.image("player.png")

enemy0_image = pyglet.resource.image("enemy0.png")
enemy0_seq = pyglet.image.ImageGrid(enemy0_image, 1, 2)

enemy1_image = pyglet.resource.image("enemy1.png")
enemy1_seq = pyglet.image.ImageGrid(enemy1_image, 1, 2)

enemy2_image = pyglet.resource.image("enemy2.png")
enemy2_seq = pyglet.image.ImageGrid(enemy2_image, 2, 2)

enemy_resources = [enemy0_seq, enemy1_seq, enemy2_seq]

invader1_image = pyglet.resource.image("invader.png")
bullet_image = pyglet.resource.image("bullet.png")


center_image(player_image)
center_image(invader1_image)
center_image(bullet_image)
