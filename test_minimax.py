from unittest import TestCase

import algorithms
import moves
import othello
from othello import W, B


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

        def utility_fn(s):
            if othello.determine_winner(s) == W:
                return 1
            else:
                return -1

        possible_moves = moves.available_moves(state, player)

        action = algorithms.minimax(state, player, utility_fn)

        self.assertTrue(action in possible_moves)

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

        def utility_fn(s):
            if othello.determine_winner(s) == B:
                return 1
            else:
                return -1

        possible_moves = moves.available_moves(state, player)

        action = algorithms.minimax(state, player, utility_fn)

        self.assertTrue(action in possible_moves)