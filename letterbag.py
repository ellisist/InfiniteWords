class Letterbag:
    """provides a way to get next 'random' letter tile"""
    def __init__(self):
        self.tiles = []
        # TODO: populate tiles with appropriate distribution of tiles

    def get_letter(self):
        # this can be rewritten to do whatever.
        return self.tiles.pop()
