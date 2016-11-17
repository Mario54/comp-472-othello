from unittest import TestCase

import algorithms
import moves
import othello
from othello import W, B


def simple_cutoff_test(state, depth):
    return othello.is_completed(state) or depth == 10


def heuristic(state):
    return len(moves.find_tiles(state, state.player)) - len(moves.find_tiles(state, othello.other_player(state.player)))


class TestMinimax(TestCase):
    def test_minimax_returns_an_action_for_white(self):
        state = othello.State((
            (W, W, W, W, W, W, W, W),
            (W, W, W, W, 0, W, W, W),
            (W, B, B, W, W, W, W, W),
            (W, W, B, W, W, W, W, 0),
            (W, W, W, B, W, W, B, W),
            (B, W, W, W, B, W, 0, B),
            (B, W, W, W, B, B, W, B),
            (B, W, W, W, B, W, W, B)
        ), player=W)

        possible_moves = moves.available_moves(state)

        action = algorithms.minimax(possible_moves, state,
                                    cutoff_test=simple_cutoff_test,
                                    heuristic_fn=heuristic)

        self.assertTrue(1 <= action <= len(possible_moves))

    def test_minimax_returns_an_action_for_black(self):
        state = othello.State((
            (W, W, W, W, W, W, W, W),
            (W, W, W, W, 0, W, W, W),
            (W, B, B, W, W, W, W, W),
            (W, W, B, W, W, W, W, 0),
            (W, W, W, B, W, W, W, W),
            (B, W, W, W, B, W, W, B),
            (B, W, W, W, B, B, W, B),
            (B, W, W, W, B, W, W, B)
        ), player=B)

        possible_moves = moves.available_moves(state)

        action = algorithms.minimax(possible_moves, state,
                                    cutoff_test=simple_cutoff_test,
                                    heuristic_fn=heuristic)

        self.assertTrue(1 <= action <= len(possible_moves))
