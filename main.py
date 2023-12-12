import json
from TicTacToe.game import Game
from player import *
from TicTacToe.player import Stupid_IA_Player

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}

import tensorflow_decision_forests as tfdf
import tensorflow as tf
import logging
tf.get_logger().setLevel(logging.NOTSET)
tf.autograph.set_verbosity(3)


player1: Player
player2: Player

# option = int(input("1 - Humano vs IA\n2 - IA vs Humano\n"))

# if option == 1:
#     player1 = Human_Player(game)
#     player2 = IA_Player(game, "player2")
# else:
#     player1 = IA_Player(game, "player1")
#     player2 = Human_Player(game)

game: Game = Game()
player1 = Stupid_IA_Player(game)
player2 = Stupid_IA_Player(game)
wins_draws = []
for x in range(1000000):

    game.reset()
    
    while not game.finished():
        game.play(player1.nextMove())

        if game.finished():
            break

        game.play(player2.nextMove())

        pass

    
    game.print_state()
    print()
    print("Fim de jogo")
    print("Vencedor: {}".format(game.winner()))
    print("Empate: {}".format(game.draw()))

    wins_draws.append({
        "winner": game.winner(),
        "draw": game.draw()
    })

    
json.dump(wins_draws, open("win_draws_with_stupids", 'w'))
print("finished")

