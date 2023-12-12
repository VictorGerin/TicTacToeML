import unittest

from TicTacToe.game import Game
from TicTacToe.satateGenerator import RawStateGenerator
from TicTacToe.satateGenerator import StateGenerator


class TestStateGenerator(unittest.TestCase):
    def test_raw_generator_count(self):

        count = 0
        for x in RawStateGenerator():
            count += 1
        self.assertEqual(count, 19683)

        pass

    def test_generator(self):
        game = Game()

        for state in StateGenerator(Game.player1):
            game.set_state(state)
            self.assertFalse(game.finished())
            
            aggr = sum([1 if x == Game.player1 else -1 if x == Game.player2 else 0 for x in state])
            self.assertEqual(aggr, 0)

        for state in StateGenerator(Game.player2):
            game.set_state(state)
            self.assertFalse(game.finished())
            
            aggr = sum([1 if x == Game.player1 else -1 if x == Game.player2 else 0 for x in state])
            self.assertEqual(aggr, 1)

        pass

    def test_generator_equals(self):
        p1_states = [x for x in StateGenerator(Game.player1)]
        for p2_state in StateGenerator(Game.player2):
            self.assertFalse(p2_state in p1_states)
            pass
        pass

    pass