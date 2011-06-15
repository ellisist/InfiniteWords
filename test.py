import game, player, board, letterbag

players = [player.Player("Player " + str(n+1)) for n in range(3)]
g = game.Game(board.Board(),letterbag.Letterbag(),players)

print g # .scoreboard()
