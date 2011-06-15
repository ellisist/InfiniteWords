class Word:
    def __init__(self):
        self.squares = []

    def __init__(self, squares):
        self.squares = squares

    def get_score(self):
        score = 0;
        for s in squares:
            score += s.score
        return score
