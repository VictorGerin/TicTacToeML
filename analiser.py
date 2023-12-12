import json
import csv
import os
from TicTacToe.game import Game
from TicTacToe.satateGenerator import StateGenerator

game = Game()

defences = [
    [0, 1, 2],
    [1, 2, 0],
    [3, 4, 5],
    [4, 5, 3],
    [6, 7, 8],
    [7, 8, 6],
    [0, 3, 6],
    [3, 6, 0],
    [1, 4, 7],
    [4, 7, 1],
    [2, 5, 8],
    [5, 8, 2],
    [0, 4, 8],
    [4, 8, 0],
    [2, 4, 6],
    [4, 6, 2],
    [0, 2, 1],
    [3, 5, 4],
    [6, 8, 7],
    [0, 6, 3],
    [1, 7, 4],
    [2, 8, 5],
    [0, 8, 4],
    [2, 6, 4],
]

def find_defence(game, current_state, player):
    enemy = Game.player1 if player == Game.player2 else Game.player2
    for defence in defences:
        filtro = [current_state[index] for index in defence]
        if filtro[-1] != Game.empty:
            continue

        if filtro[0] == enemy and filtro[1] == enemy:
            return defence[-1]
    return -1

def find_best_play(game, current_state, player):
    for i in range(9):
        if not game.empty_pos(i):
            continue
        game.play(i)
        if game.winner() == player:
            return i
        else:
            game.set_state(current_state.copy())
        pass
    game.set_state(current_state.copy())
    return -1


def main():
    player = Game.player2
    file = 'player2_states'
    fileJson = file + '.json'
    fileCsv = file + '.csv'


    if not os.path.exists(file):
        states = [{"state": x.copy(), "selected": -1} for x in StateGenerator()]
        json.dump(states, open(fileJson, 'w'))
        pass

    states = json.load(open(fileJson, 'r'))

    total = len(states)

    for i, x in enumerate(states):
        if x["selected"] != -1:
            continue

        print('------ {} {:.2f}'.format(i, i * 100 / total))
        game.set_state(x["state"].copy())
        game.print_state()

        # se houver so uma jogada faltando
        if game.qtd_empty() == 1:
            x["selected"] = game.first_empty()
            print("empty {}".format(x["selected"]))
            json.dump(states, open(fileJson, 'w'))
            continue

        # se tem uma jogado ganhadora
        best_play = find_best_play(game, x["state"], player)
        if best_play != -1:
            print("best_play {}".format(best_play))
            x["selected"] = best_play
            json.dump(states, open(fileJson, 'w'))
            continue

        # se n tem como ganhar mas vai perder na prox defende então
        defesa = find_defence(game, x["state"], player)
        if defesa != -1:
            print("Defesa {}".format(defesa))
            x["selected"] = defesa
            json.dump(states, open(fileJson, 'w'))
            continue

        # se houver so duas jogada faltando e n tiver tido defesa e nem jogada ganhadora
        # entao sera um empate e marca qlq uma das duas
        if game.qtd_empty() == 2:
            x["selected"] = game.first_empty()
            print("empty2 {}".format(x["selected"]))
            json.dump(states, open(fileJson, 'w'))
            continue


        index = input()
        x["selected"] = int(index)
        json.dump(states, open(fileJson, 'w'))
        pass

    print("Finalizado !")

    states = json.load(open(fileJson, 'r'))

    with open(fileCsv, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for x in states:
            spamwriter.writerow(x["state"] + [x["selected"]])

    pass

if __name__== "__main__":
    main()

