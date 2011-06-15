class Tile:
    def __init__(self):
        self.letter = ""
        self.score = 0

    def __init__(self,letter,score):
        self.letter = letter
        self.score = score

    def __init__(self,letter):
        #TODO: use default score
        self.letter = letter
       # self.score = game.get_score(letter)
        
