import random
from collections import namedtuple

from time_limit import time_limit, TimeoutException

W = '⬤'
B = '◯'

INITIAL_BOARD = (
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
    """
    Checks if a game is completed (if none of the player can move).
    """
    import moves

    state_other_player = State(state.board, other_player(state.player))

    return len(moves.available_moves(state)) == 0 and \
           len(moves.available_moves(state_other_player)) == 0


def determine_winner(state):
    num_black_tiles = count_tiles(state, B)
    num_white_tiles = count_tiles(state, W)

    if num_black_tiles == num_white_tiles:
        return None

    return B if num_black_tiles > num_white_tiles else W


def count_tiles(state, player):
    return len([tile for row in state.board for tile in row if tile == player])


def other_player(current_player):
    return B if current_player == W else W


class State:
    """
    Represents a state in the othello game. It stores the state of the board and the current player.
    """
    def __init__(self, board=INITIAL_BOARD, player=B):
        self.player = player
        self.board = board

    def switch_player(self):
        self.player = other_player(self.player)

    def get_tile(self, position):
        return self.board[position.y][position.x]

    def __eq__(self, other):
        return self.board == other.board

    @property
    def empty_tiles(self):
        return sum([1 for row in self.board for tile in row if tile == 0])


class BaseGame:
    def __init__(self):
        self.state = State()

    def switch_player(self):
        self.state.switch_player()

    def before_move(self):
        return ''


def run(game):
    """
    Executes an othello game, taking in a game object that inherits from BaseGame.
    It returns when the game has completed.
    """
    import moves

    while True:
        print(game.before_move(), end='')

        possible_moves = list(moves.available_moves(game.state))

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
            game.state = moves.move(game.state, possible_moves[choice - 1].position)
        except IndexError:
            print('Invalid move! Try again.')
            continue
        except moves.InvalidMove:
            print('Invalid move! Try again.')
            continue

        game.switch_player()
