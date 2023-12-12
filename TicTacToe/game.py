from functools import reduce

import sys
from typing import IO

"""
A Class that represents a TicTacToe game
See test/test_game for usage examples
"""
class Game:
    player1 = 'X'
    player2 = 'Y'
    empty = ' '

    __win_patterns__ = [
        [0, 1, 2],  # horizontal
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],  # vertical
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],  # diagonal
        [2, 4, 6]
    ]

    def __init__(self):
        self.__state__ = []
        self.__current_player__ = Game.player1
        self.set_state([Game.empty for i in range(9)])
        pass

    def reset(self):
        """Resets game state as a new game has been started"""
        self.__state__ = []
        self.__current_player__ = Game.player1
        self.set_state([Game.empty for i in range(9)])

    def empty_pos(self, position) -> bool:
        """return if the position is free"""
        if position < 0 or position > self.__state__.__len__():
            raise Exception('Invalid play!')
        return self.__state__[position] == Game.empty

    def play(self, position):
        """Make a play on the position with current player"""
        if position < 0 or position > self.__state__.__len__():
            raise Exception('Invalid play!')
        if not self.empty_pos(position):
            raise Exception('Invalid play!')

        self.__state__[position] = self.__current_player__
        self.__current_player__ = self.player2 if self.__current_player__ == self.player1 else self.player1
        pass

    def finished(self) -> bool:
        """Return true if the game has finish"""
        return self.winner() or self.draw()

    def winner(self) -> str | bool:
        """Return the winner of the game or False if there is no winner"""
        for pattern in self.__win_patterns__:
            winner = self.__teste_pattern(pattern)
            if winner:
                return winner
        return False

    def __teste_pattern(self, pattern):
        line_state = [self.__state__[index] for index in pattern]
        # se no pattern tiver 3 X ou 3 O, retorna true
        return line_state[0] if len(set(line_state)) == 1 and line_state[0] != Game.empty else False

    def qtd_winner(self) -> int:
        """Return the amount ways the winner parrten has been fullfill"""
        count = 0
        for pattern in self.__win_patterns__:
            if self.__teste_pattern(pattern):
                count += 1
        return count

    def first_empty(self) -> int:
        """Return the first index with is empty or -1 if there is none"""
        for i, x in enumerate(self.__state__):
            if x == Game.empty:
                return i
        return -1

    def qtd_empty(self) -> int:
        """Return the amount of spaces is left to be played"""
        return sum([1 if x == Game.empty else 0 for x in self.__state__])

    def draw(self) -> bool:
        """Return if the game has finished with a draw"""
        no_space_left = reduce(lambda a, b: a and b, [x != Game.empty for x in self.__state__], True)
        return no_space_left and not self.winner()


    def set_state(self, state):
        """
        Set the game current state (the table parrten)
        param state should be a array of Game.player1, Game.player2 and Game.empty
        """
        self.__state__ = state

        # se tiver a mesma qtd de X e O então o prox e X, senao e O e o prox
        aggr = sum([1 if x == self.player1 else -1 if x == self.player2 else 0 for x in state])
        self.__current_player__ = aggr == 0 and self.player1 or self.player2

        pass

    def print_state(self, file: IO[str] = sys.stdout, emptyToIndex: bool = True):
        """Print the current game state"""
        for i in range(3):
            for j in range(3):
                to_be_printed = self.__state__[i * 3 + j]
                to_be_printed = to_be_printed if to_be_printed != Game.empty else i * 3 + j if emptyToIndex else to_be_printed
                print(to_be_printed, end=' ', file=file)
            print('', file=file)

        pass
