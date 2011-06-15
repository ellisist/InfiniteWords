import player, board, letterbag, StringIO

class Game:
    """Contains all objects associated with a given game"""
    def __init__(self):
        self.board = board.Board()
        self.letterbag = letterbag.Letterbag()
        self.players = []

    def __init__(self,my_board,my_letterbag,my_players):
        self.board = my_board
        self.letterbag = my_letterbag
        self.players = my_players

    def scoreboard(self):
        return [(p.name,p.score) for p in self.players]

    def __str__(self):
        s = StringIO.StringIO()
        print >>s, "Game:", id(self)
        print >>s, "Scoreboard:"
        print >>s, self.scoreboard()
        print >>s, self.board
        return s.getvalue()

