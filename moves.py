from collections import namedtuple
from itertools import product

from othello import B, W

Position = namedtuple('Position', ['x', 'y'])
Move = namedtuple('Move', ['position', 'reversals'])


def find_tiles(state, player):
    all_positions = [Position(x=p[0], y=p[1]) for p in product(range(0, 8), repeat=2)]

    return tuple([p for p in all_positions if get_tile(state, position=p) == player])


def get_tile(state, position):
    return state[position.y][position.x]


def find_move(state, player, position_sequence):
    opposite_player = B if player == W else W

    valid = False
    reversals = []

    for index, pos in enumerate(position_sequence):
        tile = get_tile(state, pos)

        if tile == 0:
            return Move(pos, reversals) if valid else None
        if tile == opposite_player:
            valid = True
            reversals.append(pos)
        if tile == player:
            return


def column_sequences(pos):
    return tuple([Position(y=n, x=pos.x) for n in range(pos.y + 1, 8)]), \
           tuple(reversed([Position(y=n, x=pos.x) for n in range(0, pos.y)]))


def row_sequences(pos):
    return tuple([Position(x=n, y=pos.y) for n in range(pos.x + 1, 8)]), \
           tuple(reversed([Position(x=n, y=pos.y) for n in range(0, pos.x)]))


def diagonal_sequence(pos, x_inc, y_inc):
    x_max = 7 if x_inc == 1 else 0
    y_max = 7 if y_inc == 1 else 0

    return tuple([Position(x=i[0], y=i[1])
                  for i in zip(range(pos.x + x_inc, x_max + x_inc, x_inc), range(pos.y + y_inc, y_max + y_inc, y_inc))
                  if i[0] <= 7 and i[0] <= 7])


def diagonal_sequences(pos):
    return (diagonal_sequence(pos, x_inc=-1, y_inc=-1), diagonal_sequence(pos, x_inc=-1, y_inc=1), diagonal_sequence(
        pos, x_inc=1, y_inc=-1), diagonal_sequence(pos, x_inc=1, y_inc=1))


def linear_sequences(position):
    return column_sequences(position) + row_sequences(position) + diagonal_sequences(position)


def moves(state, player, position):
    pos_sequences = linear_sequences(position)

    valid_moves = [m for m in
                   [find_move(state, player, pos_sequence) for pos_sequence in pos_sequences if pos_sequences] if m]

    return tuple(valid_moves)


def flatten(lst):
    return [item for sub_list in lst for item in sub_list]


def available_moves(state, player):
    """

    :param state: Board (8x8 tuple)
    :param player: 'W' or 'B'
    """
    avail_moves = flatten([moves(state, player, position) for position in find_tiles(state, player)])

    move_dict = {}

    for m in avail_moves:
        if m.position in move_dict:
            for reversal in m.reversals:
                move_dict[m.position].add(reversal)
        else:
            move_dict[m.position] = set(m.reversals)

    return set([Move(pos, tuple(reversals)) for (pos, reversals) in move_dict.items()])


class InvalidMove(Exception):
    pass


def copy_state(state):
    return [list(row) for row in state]


def move(state, player, position):
    possible_moves = available_moves(state, player)
    valid_positions = [m.position for m in possible_moves]

    if position in valid_positions:
        new_state = copy_state(state)

        reversals = list(dict(possible_moves)[position]) + [position]

        for pos in reversals:
            new_state[pos.y][pos.x] = player

        return tuple([tuple(row) for row in new_state])

    raise InvalidMove
