from unittest import TestCase

from othello import B, W, is_completed, State


class TestOthello(TestCase):
    def test_is_completed(self):
        board = (
            (0, B, B, B, B, W, W, W,),
            (B, B, B, B, B, B, B, B,),
            (B, B, B, B, B, B, B, B,),
            (B, B, W, B, B, B, B, W,),
            (B, B, W, B, B, B, W, W,),
            (B, B, W, B, B, 0, W, W,),
            (B, W, W, W, W, W, W, W,),
            (0, B, B, B, B, B, B, W,),
        )

        state = State(board, B)

        self.assertFalse(is_completed(state))
