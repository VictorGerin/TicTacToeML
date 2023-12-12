import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}

from TicTacToe.player import Player
import tensorflow as tf
import logging
tf.get_logger().setLevel(logging.NOTSET)
tf.autograph.set_verbosity(3)


class IA_Player(Player):
    
        def __init__(self, game, model):
            super().__init__(game)
            self.model = tf.keras.models.load_model(model)

        def createds_from_state(self, state):
            tf_dataset = tf.data.Dataset.from_tensor_slices(
                ({
                    "x0": [state[0]],
                    "x1": [state[1]],
                    "x2": [state[2]],
                    "x3": [state[3]],
                    "x4": [state[4]],
                    "x5": [state[5]],
                    "x6": [state[6]],
                    "x7": [state[7]],
                    "x8": [state[8]],
                },
                [0],
            )).batch(1)
            return tf_dataset
    
        def nextMove(self):
            IA_play = [(index, x) for index, x in enumerate(self.model.predict(
                self.createds_from_state(self.game.__state__),
                verbose=None
                )[0])]
            IA_play.sort(key=lambda a: a[1], reverse=True)
            IA_play = [x[0] for x in IA_play if self.game.empty_pos(x[0])]
            return IA_play[0]