import tile

class Square:
    """representing a square on the game board"""
    def __init__(self):
        # start at origin
        self.x = 0;
        self.y = 0;
        # self.mod  #havent decided what form mod will take yet.
        self.tile = tile.Tile()
