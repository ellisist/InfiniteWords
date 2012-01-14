import StringIO, itertools

class Player:
    """representation of a player in the game"""
    def __init__(self):
        #self.score = 0
        self.tiles = []
        self.words = []
        self.name = ""
    def __init__(self, name):
        #self.score = 0
        self.tiles = []
        self.words = []
        self.name = str(name)

    def score(self):
        return sum([w.score for w in self.words])

    def __str__(self):
        s = StringIO.StringIO()
        print >>s, "Player:", self.name + ':', self.score()
        print >>s, "Tiles:", self.tiles
        print >>s, "Words:", self.words
        return s.getvalue()

    def playword(self,tiles,squares):
        for tile, square in itertools.izip(tiles,squares):
            square.tile = tile
        self.words.append(Word(squares))
