import random

import moves
from time_limit import time_limit, TimeoutException

W = 'W'
B = 'B'

INITIAL_STATE = (
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, W, B, 0, 0, 0),
    (0, 0, 0, B, W, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0)
)


def is_completed(state):
    return len(moves.available_moves(state, B)) == 0 and \
           len(moves.available_moves(state, W)) == 0


def determine_winner(state):
    num_black_tiles = count_tiles(state, B)
    num_white_tiles = count_tiles(state, W)

    if num_black_tiles == num_white_tiles:
        return None

    return B if num_black_tiles > num_white_tiles else W


def count_tiles(state, player):
    return len([tile for row in state for tile in row if tile == player])


def other_player(current_player):
    return B if current_player == W else W


class BaseGame:
    def __init__(self):
        self.player = B
        self.state = INITIAL_STATE

    def switch_player(self):
        self.player = other_player(self.player)

    def before_move(self):
        return ''


def run(game):
    while True:
        print(game.before_move(), end='')

        possible_moves = list(moves.available_moves(game.state, game.player))

        if is_completed(game.state):
            return game.announce_winner()

        if len(possible_moves) == 0:
                game.switch_player()
                continue

        game.draw_board(possible_moves)

        try:
            with time_limit(30):
                choice = game.input(possible_moves)
        except TimeoutException:
            choice = random.randint(1, len(possible_moves))
            print("Turn time limit exceeded. Picking random move.")

        try:
            game.state = moves.move(game.state, game.player, possible_moves[choice - 1].position)
        except IndexError:
            print('Invalid move! Try again.')
            continue
        except moves.InvalidMove:
            print('Invalid move! Try again.')
            continue

        game.switch_player()
