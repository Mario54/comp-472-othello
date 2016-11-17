from unittest import TestCase

import algorithms
import moves
import othello
from othello import W, B


def simple_cutoff_test(state, depth):
    return othello.is_completed(state) or depth == 10


def heuristic(board, player):
    len(moves.find_tiles(board, player)) - len(moves.find_tiles(board, othello.other_player(player)))


class TestMinimax(TestCase):
    def test_minimax_returns_an_action_for_white(self):
        state = (
            (W, W, W, W, W, W, W, W),
            (W, W, W, W, 0, W, W, W),
            (W, B, B, W, W, W, W, W),
            (W, W, B, W, W, W, W, 0),
            (W, W, W, B, W, W, B, W),
            (B, W, W, W, B, W, 0, B),
            (B, W, W, W, B, B, W, B),
            (B, W, W, W, B, W, W, B)
        )

        player = W

        possible_moves = moves.available_moves(state, player)

        action = algorithms.minimax(possible_moves, state, player,
                                    cutoff_test=simple_cutoff_test,
                                    heuristic_fn=heuristic)

        self.assertTrue(0 <= action < len(possible_moves))

    def test_minimax_returns_an_action_for_black(self):
        state = (
            (W, W, W, W, W, W, W, W),
            (W, W, W, W, 0, W, W, W),
            (W, B, B, W, W, W, W, W),
            (W, W, B, W, W, W, W, 0),
            (W, W, W, B, W, W, W, W),
            (B, W, W, W, B, W, W, B),
            (B, W, W, W, B, B, W, B),
            (B, W, W, W, B, W, W, B)
        )

        player = B

        possible_moves = moves.available_moves(state, player)

        action = algorithms.minimax(possible_moves, state, player,
                                    cutoff_test=simple_cutoff_test,
                                    heuristic_fn=heuristic)

        self.assertTrue(0 <= action < len(possible_moves))
