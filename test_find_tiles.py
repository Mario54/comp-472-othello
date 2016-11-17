from unittest import TestCase

import moves
from othello import State, W, B


class TestFindTiles(TestCase):
    def test_find_tiles_white(self):
        board = (
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, W, B, 0, 0, 0),
            (0, 0, 0, B, W, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0)
        )

        state = State(board, player=W)

        expected = ((3, 3), (4, 4))

        actual = moves.find_tiles(state)

        self.assertEqual(set(expected), set(actual))

    def test_find_tiles_black(self):
        board = (
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, W, B, 0, 0, 0),
            (0, 0, 0, B, W, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0)
        )

        state = State(board, player=B)

        expected = ((4, 3), (3, 4))

        actual = moves.find_tiles(state)

        self.assertEqual(set(expected), set(actual))

    def test_find_tiles_edge(self):
        board = (
            (B, 0, 0, 0, 0, 0, 0, B),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, W, B, 0, 0, 0),
            (0, 0, 0, B, W, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (B, 0, 0, 0, 0, 0, 0, B)
        )

        state = State(board, player=B)

        expected = ((4, 3), (3, 4), (0, 0), (7, 0), (0, 7), (7, 7))

        actual = moves.find_tiles(state)

        self.assertEqual(set(expected), set(actual))
