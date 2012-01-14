import StringIO

class Board:
    """represents the board"""
    def __init__(self):
        self.squares = []
    def drawBoard(self):
        print "Drawing board..."
    def __str__(self):
        s = StringIO.StringIO()
        print >>s, "Board:", id(self)
        print >>s, self.squares
        return s.getvalue()
    def getSquare(x,y):
        # first check if square is in squares if it is, return it.  
        
        #if not, make a new square, add it to squares, then return.
        
        
