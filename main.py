
import logging
from classes.game import Game

logger = logging.getLogger(__name__)
if __name__ == "__main__":
    logger.info("Game starts now!")
    g = Game()
    g.main()
