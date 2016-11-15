from operator import itemgetter

import math

import moves
import othello


def maximize_reversals(possible_moves):
    return possible_moves.index(max(possible_moves, key=lambda m: len(m.reversals))) + 1


def minimax(state, player, utility_fn):
    full_state = (state, player)

    def actions(s):
        return moves.available_moves(s[0], s[1])

    def terminal_test(st):
        return othello.is_completed(st)

    def result(s, a):
        return moves.move(s[0], s[1], a.position), othello.other_player(s[1])

    def max_value(s, alpha, beta):
        if terminal_test(s[0]):
            return utility_fn(s[0])

        v = -math.inf

        for action in actions(s):
            # Take the max b/c we are taking max's perspective
            v = max(v, min_value(result(s, action), alpha, beta))

            if v >= beta:
                # prune because we found an action which is better for max than the action associated with beta
                # so, min will never take this action
                return v

            alpha = max(v, alpha)

        return v

    def min_value(s, alpha, beta):
        if terminal_test(s[0]):
            return utility_fn(s[0])

        v = math.inf

        for action in actions(s):
            # Take the min b/c we are taking min's perspective
            v = min(v, max_value(result(s, action), alpha, beta))

            if v <= alpha:
                # prune because min would take an action that is worst for max than the action associated with alpha
                # so, max will never take the current action
                return v

            beta = min(beta, v)

        return v

    best_action = None
    best_value = -math.inf

    for a in actions(full_state):
        action_value = min_value(result(full_state, a), best_value, math.inf)

        if action_value >= best_value:
            best_value = action_value
            best_action = a

    return best_action