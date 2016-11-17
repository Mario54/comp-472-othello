import math

import moves
import othello


def maximize_reversals(possible_moves):
    return possible_moves.index(max(possible_moves, key=lambda m: len(m.reversals))) + 1


def minimax_mario(valid_moves, state):
    """
    Gives more value if the player has more tiles.
    :param board:
    :param player:
    :return:
    """

    def heuristic(state):
        return len(moves.find_tiles(state)) - len(moves.find_tiles(state, othello.other_player(state.player)))

    def simple_cutoff_test(state, depth):
        return othello.is_completed(state) or depth == 4

    return minimax(valid_moves, state, simple_cutoff_test, heuristic)


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
            v = max(v, min_value(result(s, action), alpha, beta, depth+1))

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
