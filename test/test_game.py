import unittest

from TicTacToe.game import Game


class TestGame(unittest.TestCase):
    def teste_X_win(self):
        jogo = Game()

        jogo.play(0)  # X
        jogo.play(3)  # Y
        jogo.play(1)  # X
        jogo.play(4)  # Y
        self.assertFalse(jogo.winner())
        self.assertFalse(jogo.finished())
        jogo.play(2)  # X
        self.assertEqual(jogo.winner(), Game.player1)
        self.assertTrue(jogo.finished())

    def teste_O_win(self):
        jogo = Game()

        jogo.set_state([Game.player1, Game.player1, Game.empty,
                        Game.player2, Game.player2, Game.empty,
                        Game.player1, Game.empty, Game.empty])

        self.assertFalse(jogo.winner())
        self.assertFalse(jogo.finished())
        jogo.play(5)
        self.assertEqual(jogo.winner(), Game.player2)
        self.assertTrue(jogo.finished())

    def test_draw(self):
        jogo = Game()

        jogo.set_state([Game.player1, Game.player1, Game.player2,
                        Game.player2, Game.player2, Game.player1,
                        Game.player1, Game.player1, Game.player2])

        self.assertTrue(jogo.draw())
        self.assertTrue(jogo.finished())
    
    def test_reset(self):
        jogo = Game()

        jogo.set_state([Game.player1, Game.player1, Game.player2,
                        Game.player2, Game.player2, Game.player1,
                        Game.player1, Game.player1, Game.player2])

        self.assertTrue(jogo.draw())
        self.assertTrue(jogo.finished())

        jogo.reset()

        self.assertEqual(jogo.__state__, [Game.empty for x in range(9)])

