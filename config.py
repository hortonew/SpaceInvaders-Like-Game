WINDOW_SIZE = (1024, 768)
ENEMY_MARGIN = (60, 40)
ENEMY_SPEED = 5
ENEMY_BULLET_SPEED = -350.0
ENEMY_ANIM_SPEED = .5
NUM_ENEMIES = 20
PLAYER_THRUST = 300.0
PLAYER_LIVES = 3
PLAYER_BULLET_SPEED = 700.0
SPRITE_SCALE = 2 
MYSTERY_SCORE_NUMBER = 7
LOGGING = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    },
}

import logging.config
logging.config.dictConfig(LOGGING)
