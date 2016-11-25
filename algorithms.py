import math

import moves
import othello
import utils


def maximize_reversals(possible_moves):
    return possible_moves.index(max(possible_moves, key=lambda m: len(m.reversals))) + 1


def minimax_mario(valid_moves, current_state):
    corners = ((0, 0), (0, 7), (7, 0), (7, 7))

    def heuristic(state):
        corner_feature = len([corner for corner in corners if state.board[corner[1]][corner[0]]])
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
        corner_feature = len([corner for corner in corners if state.board[corner[1]][corner[0]]])
        near_corner_feature = len([pos for pos in near_corner if state.board[pos[1]][pos[0]]])
        tiles_count = len(moves.find_tiles(state)) - len(moves.find_tiles(state, othello.other_player(state.player)))
        count_moves = len(moves.available_moves(state))
        immune_tiles = len(utils.immune_tiles(state))

        corner_feature_value = 5
        near_corner_value = -1
        tiles_count_value = 1
        count_moves_value = 2

        near_end_of_game = state.empty_tiles < 10
        early_game = state.empty_tiles > 35

        if early_game:
            immune_tiles_value = 1/4
        elif near_end_of_game:
            tiles_count_value = 2
            immune_tiles_value = 1/4
        else:
            immune_tiles_value = 1/4

        return corner_feature * corner_feature_value + \
            near_corner_feature * near_corner_value + \
            tiles_count * tiles_count_value + \
            count_moves * count_moves_value + \
            immune_tiles * immune_tiles_value

    def simple_cutoff_test(state, depth):
        return othello.is_completed(state) or depth == 3

    return minimax(valid_moves, current_state, simple_cutoff_test, heuristic)


def minimax(valid_moves, state, cutoff_test, heuristic_fn):
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
