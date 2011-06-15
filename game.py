import player, board, letterbag

class Game:
    """Contains all objects associated with a given game"""
    def __init__(self):
        self.board = board.Board()
        self.letterbag = letterbag.Letterbag()
        self.players = []
    def print_scoreboard(self):
        for p in players:
            print p.name, p.score

