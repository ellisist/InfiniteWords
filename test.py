import game, player, board, letterbag

players = [player.Player("Player " + str(n+1)) for n in range(3)]
g = game.Game(board.Board(),letterbag.Letterbag(),players)


# turn generator
t = g.taketurns()

print g

i = 0
while(i < 5):
    player = t.next()
    player.playword(self,)
    i += 1


