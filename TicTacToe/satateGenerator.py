from functools import reduce
from game import Game

class RawStateGenerator:
    __ordem__ = [Game.empty, Game.player1, Game.player2]

    def __init__(self):
        self.__state__ = [Game.empty for i in range(9)]
        self.finished = False
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.finished:
            raise StopIteration

        self.add(8, [1, 0, 0, 0, 0, 0, 0, 0, 0])

        # voltou tudo p/ o estado inicial então retorna ele e no prox para
        self.finished = reduce(lambda a, b: a and b, [x == self.__ordem__[0] for x in self.__state__], True)

        return self.__state__
        pass

    def add(self, index, amount):

        if index < 0:
            return False

        vem_um = self.add(index - 1, amount)

        amount[index] += 1 if vem_um else 0
        amount[index] += self.__ordem__.index(self.__state__[index])

        self.__state__[index] = self.__ordem__[amount[index] % len(self.__ordem__)]

        return amount[index] >= len(self.__ordem__)
        pass

    pass


class StateGenerator:
    def __init__(self):
        self.__game__ = Game()
        self.__raw_generator__ = iter(RawStateGenerator())
        pass

    def __iter__(self):
        return self

    def __next__(self):

        while True:
            state = self.__raw_generator__.__next__()
            self.__game__.set_state(state)

            if self.__game__.draw():
                continue

            # Se O tiver jogado mais q X ou X tiver jogador 2 mais q O, pula para o proximo estado
            aggr = sum([1 if x == Game.player1 else -1 if x == Game.player2 else 0 for x in state])
            if aggr != 1:
                continue

            # se tiver mais de 1 vencedor, pula para o proximo estado
            if self.__game__.qtd_winner() > 0:
                continue

            # if self.__game__.draw():
            #     continue

            break

            pass

        return state
        pass
