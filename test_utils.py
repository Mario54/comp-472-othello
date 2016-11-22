from unittest import TestCase

import utils
from moves import Position
from othello import B, W, State


class TestUtils(TestCase):
    def test_immune_tiles(self):
        board = (
            (W, 0, 0, W, 0, 0, 0, 0),
            (0, W, 0, W, 0, 0, 0, 0),
            (0, 0, W, W, 0, 0, 0, 0),
            (W, W, W, W, B, 0, 0, 0),
            (0, 0, W, B, W, 0, 0, 0),
            (0, W, 0, 0, 0, 0, 0, 0),
            (W, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0)
        )

        state = State(board, player=W)

        expected = {
            Position(0, 0),
            Position(3, 3),
        }

        self.assertEqual(
            set(utils.immune_tiles(state)),
            expected
        )



