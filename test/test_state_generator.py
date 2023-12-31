import unittest

from TicTacToe.game import Game
from TicTacToe.satateGenerator import RawStateGenerator
from TicTacToe.satateGenerator import StateGenerator


class TestStateGenerator(unittest.TestCase):
    def test_raw_generator_count(self):

        count = 0
        for x in RawStateGenerator():
            count += 1
        """for each slot in the state has 3 options since there is 9 slots the amount of combinations is 3^9"""
        self.assertEqual(count, 3 ** 9)

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

    def test_p2_states(self):
        p1_states = [x.copy() for x in StateGenerator(Game.player1)]

        #Nenhum estado d p2 deve está contido em p1
        for p2_state in StateGenerator(Game.player2):
            self.assertFalse(p2_state in p1_states)
            pass
        pass

    def test_p1_states(self):
        p2_states = [x.copy() for x in StateGenerator(Game.player2)]

        #Nenhum estado d p2 deve está contido em p1
        for p1_state in StateGenerator(Game.player1):
            self.assertFalse(p1_state in p2_states)
            pass
        pass

    pass