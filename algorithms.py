import math

import moves
import othello
import utils


def maximize_reversals(possible_moves):
    return possible_moves.index(max(possible_moves, key=lambda m: len(m.reversals))) + 1


def minimax_hilary(valid_moves, state):
    '''
    corners = (0,0),(0,7),(7,0),(7,7)
    x-square = (1,1),(1,6),(6,1),(6,6)
    c-square =
    (0,1)(0,6)
    (1,0)(1,7)
    (6,0)(6,7)
    (7,1)(7,6)

    Gives more value if the play reaches the corners

    - avoid x- and c-square
    - try to reach around the forbidden area

    '''

    def heuristic(state):
        h = 0
        corners = ((0, 0), (0, 7), (7, 0), (7, 7))
        x_square = ((1, 1), (1, 6), (6, 1), (6, 6))
        c_square = (
            (0, 1), (0, 6),
            (1, 0), (1, 7),
            (6, 0), (6, 7),
            (7, 1), (7, 6)
        )
        l_square = (
            (0, 2), (1, 2), (2, 2), (2, 1), (2, 0),
            (0, 5), (1, 5), (2, 5), (2, 6), (2, 7),
            (5, 0), (5, 1), (5, 2), (6, 2), (7, 2),
            (7, 5), (6, 5), (5, 5), (5, 6), (5, 7)
        )
        for move in moves.available_moves(state):
            if move.position in corners:
                h += 10
            if move.position in x_square or move.position in c_square:
                h += -1
            if move.position in l_square:
                h += 5

        return h

    def simple_cutoff_test(state, depth):
        return othello.is_completed(state) or depth == 4

    return minimax(valid_moves, state, simple_cutoff_test, heuristic)


def minimax_mario(valid_moves, current_state):
    corners = ((0, 0), (0, 7), (7, 0), (7, 7))

    def heuristic(state):
        corner_feature = len([corner for corner in corners if state.board[corner[1]][corner[0]] == state.player])
        tiles_count = len(moves.find_tiles(state)) - len(moves.find_tiles(state, othello.other_player(state.player)))
        count_moves = len(moves.available_moves(state))

        corner_feature_value = 5
        tiles_count_value = 1
        count_moves_value = 2

        near_end_of_game = state.empty_tiles < 10

        if near_end_of_game:
            tiles_count_value = 2

        return corner_feature * corner_feature_value + \
               tiles_count * tiles_count_value + \
               count_moves * count_moves_value

    def simple_cutoff_test(state, depth):
        return othello.is_completed(state) or depth == 3

    return minimax(valid_moves, current_state, simple_cutoff_test, heuristic)


def minimax_mario_2(valid_moves, current_state):
    corners = ((0, 0), (0, 7), (7, 0), (7, 7))
    near_corner = (
        (0, 1), (1, 0), (1, 1),
        (6, 0), (7, 1), (6, 1),
        (0, 6), (1, 6), (1, 7),
        (6, 6), (6, 7), (7, 6)
    )

    def heuristic(state):
        possible_moves = moves.available_moves(state)

        corner_feature = len([corner for corner in corners if state.board[corner[1]][corner[0]] == state.player])
        near_corner_feature = len([pos for pos in near_corner if state.board[pos[1]][pos[0]] == state.player])
        tiles_count = len(moves.find_tiles(state)) - len(moves.find_tiles(state, othello.other_player(state.player)))
        count_moves = len(possible_moves)
        immune_tiles = len(utils.immune_tiles(state))
        corner_in_move = len([m.position for m in possible_moves if m.position in corners])

        corner_feature_value = 15
        near_corner_value = -8
        tiles_count_value = 1 / 2
        count_moves_value = 3
        immune_tiles_value = 1 / 4
        corner_in_move_value = 1 / 2

        near_end_of_game = state.empty_tiles < 8

        if near_end_of_game:
            tiles_count_value = 2

        return corner_feature * corner_feature_value + \
               near_corner_feature * near_corner_value + \
               tiles_count * tiles_count_value + \
               count_moves * count_moves_value + \
               immune_tiles * immune_tiles_value + \
               corner_in_move * corner_in_move_value

    def simple_cutoff_test(state, depth):
        return othello.is_completed(state) or depth == 4

    return minimax(valid_moves, current_state, simple_cutoff_test, heuristic)


def minimax(valid_moves, state, cutoff_test, heuristic_fn):
    """
    Implementation for the minimax algorithm, with alpha-beta pruning, evaluation function and a cutoff test.

    Returns the index for the move that was selected from valid_moves.
    """

    def actions(s):
        return moves.available_moves(s)

    def result(s, a):
        new_state = moves.move(s, a.position)
        new_state.switch_player()

        return new_state

    def max_value(s, alpha, beta, depth):
        if cutoff_test(s, depth):
            return heuristic_fn(s)

        v = -math.inf

        for action in actions(s):
            # Take the max b/c we are taking max's perspective
            v = max(v, min_value(result(s, action), alpha, beta, depth + 1))

            if v >= beta:
                # prune because we found an action which is better for max than the action associated with beta
                # so, min will never take this action
                return v

            alpha = max(v, alpha)

        return v

    def min_value(s, alpha, beta, depth):
        if cutoff_test(s, depth):
            return heuristic_fn(s)

        v = math.inf

        for action in actions(s):
            # Take the min b/c we are taking min's perspective
            v = min(v, max_value(result(s, action), alpha, beta, depth + 1))

            if v <= alpha:
                # prune because min would take an action that is worst for max than the action associated with alpha
                # so, max will never take the current action
                return v

            beta = min(beta, v)

        return v

    best_action = None
    best_value = -math.inf

    for i, a in enumerate(valid_moves):
        action_value = min_value(result(state, a), best_value, math.inf, depth=1)

        if action_value >= best_value:
            best_value = action_value
            best_action = i

    return best_action + 1
