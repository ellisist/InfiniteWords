
class Player:
    """representation of a player in the game"""
    def __init__(self):
        self.score = 0
        self.tiles = []
        self.words = []
        self.name = ""
    def __init__(self, name):
        self.score = 0
        self.tiles = []
        self.words = []
        self.name = str(name)
