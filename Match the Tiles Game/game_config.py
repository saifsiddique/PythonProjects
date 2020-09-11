#contains constanst values for the game

import os
IMAGE_SIZE = 128        #size for each tile/animal
SCREEN_SIZE = 512

NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 4

ASSET_DIR = 'assets'
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']

assert len(ASSET_FILES) == 8    #checks if 8 files are present