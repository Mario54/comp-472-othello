from unittest import TestCase

import moves

from moves import Move

W = 'W'
B = 'B'


class TestFindNextMoves(TestCase):
    def assertSameMoves(self, first, second):
        self.assertEqual(len(first), len(second))

        moves_2_dict = {}

        for m in second:
            moves_2_dict[m.position] = m.reversals

        for m in first:
            if m.position not in moves_2_dict:
                raise AssertionError(str(m.position) + ' is in first but not in second.')

            if set(moves_2_dict[m.position]) != set(m.reversals):
                raise AssertionError(
                    str(m.position) + ' does not have the same reversals. First: {}. Second: {}'.format(m.reversals,
                                                                                                        moves_2_dict[
                                                                                                            m.position]))

    def test_find_moves_black(self):
        state = (
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, W, B, 0, 0, 0),
            (0, 0, 0, B, W, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0)
        )

        expected = (
            Move((3, 2), reversals=((3, 3),)),
            Move((2, 3), reversals=((3, 3),)),
            Move((4, 5), reversals=((4, 4),)),
            Move((5, 4), reversals=((4, 4),))
        )

        actual = moves.available_moves(state, player='B')

        self.assertEqual(set(expected), set(actual))
        self.assertEqual(len(expected), len(actual))

    def test_find_moves_black_2(self):
        state = (
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, B, 0, 0),
            (0, 0, 0, W, B, W, 0, 0),
            (0, 0, 0, B, B, 0, 0, 0),
            (0, 0, 0, 0, B, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0)
        )

        expected = (
            Move((2, 3), reversals=((3, 3),)),
            Move((3, 2), reversals=((3, 3),)),
            Move((6, 2), reversals=((5, 3),)),
            Move((6, 3), reversals=((5, 3),)),
            Move((5, 4), reversals=((5, 3),)),
            Move((2, 2), reversals=((3, 3),))
        )

        actual = moves.available_moves(state, player='B')

        self.assertEqual(set(expected), set(actual))
        self.assertEqual(len(expected), len(actual))

    def test_find_moves_black_3(self):
        state = (
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, B, W, 0, 0, 0),
            (0, 0, 0, B, W, 0, 0, 0),
            (0, 0, 0, B, W, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0)
        )

        expected = {
            Move((5, 2), reversals=((4, 2), (4, 3))),
            Move((5, 3), reversals=((4, 3),)),
            Move((5, 4), reversals=((4, 4), (4, 3))),
            Move((5, 1), reversals=((4, 2),)),
            Move((5, 5), reversals=((4, 4),))
        }

        actual = moves.available_moves(state, player='B')

        self.assertEqual(expected, actual)
        self.assertEqual(len(expected), len(actual))

    def test_find_moves_black_4(self):
        state = (
            (W, W, W, 0, W, W, W, W),
            (W, W, W, 0, 0, W, W, W),
            (W, 0, B, W, W, W, W, W),
            (W, W, W, W, W, W, W, 0),
            (W, 0, W, B, W, B, 0, W),
            (B, B, B, B, B, B, W, 0),
            (W, 0, 0, W, W, 0, 0, W),
            (0, 0, 0, W, 0, W, 0, 0)
        )

        expected = (
            Move((3, 1), reversals=((3, 2), (3, 3))),
            Move((4, 1), reversals=((4, 2), (4, 4), (4, 3))),
            Move((1, 2), reversals=((2, 3),)),
            Move((1, 4), reversals=((2, 4),)),
            Move((0, 7), reversals=((0, 6),)),
            Move((2, 7), reversals=((3, 6),)),
            Move((4, 7), reversals=((4, 6), (3, 6))),
            Move((7, 5), reversals=((6, 5),))
        )

        actual = moves.available_moves(state, player=B)

        self.assertEqual(set(expected), set(actual))
        self.assertEqual(len(expected), len(actual))

    def test_find_moves_white(self):
        state = (
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, B, 0, 0),
            (0, 0, 0, W, B, B, B, 0),
            (0, 0, 0, B, B, 0, 0, 0),
            (0, 0, 0, 0, B, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0)
        )

        expected = (
            Move((3, 5), reversals=((3, 4),)),
            Move((5, 5), reversals=((4, 4),)),
            Move((7, 3), reversals=((6, 3), (4, 3), (5, 3)))
        )

        actual = moves.available_moves(state, player='W')

        self.assertEqual(set(expected), set(actual))
        self.assertEqual(len(expected), len(actual))

    def test_find_moves_white_2(self):
        state = (
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, W, 0),
            (0, 0, 0, 0, 0, B, 0, 0),
            (0, 0, 0, 0, B, B, B, 0),
            (0, 0, 0, B, B, 0, 0, 0),
            (0, 0, 0, B, B, B, W, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0)
        )

        expected = (
            Move((2, 5), reversals=((3, 5), (4, 5), (5, 5), (3, 4), (4, 3), (5, 2))),
        )

        actual = moves.available_moves(state, player='W')

        self.assertSameMoves(expected, actual)

    def test_moves_black(self):
        state = (
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, W, B, 0, 0, 0),
            (0, 0, 0, B, W, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0)
        )

        expected = (
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, W, B, 0, 0, 0),
            (0, 0, 0, B, B, 0, 0, 0),
            (0, 0, 0, 0, B, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0)
        )

        actual = moves.move(state, player='B', position=moves.Position(4, 5))

        self.assertEqual(expected, actual)

    def test_moves_white(self):
        state = (
            (0, 0, 0, 0, 0, W, 0, 0),
            (0, 0, 0, 0, 0, W, 0, 0),
            (0, 0, 0, B, B, W, 0, 0),
            (0, 0, 0, B, B, W, 0, 0),
            (0, 0, B, B, B, W, 0, 0),
            (0, 0, 0, W, B, W, W, W),
            (0, 0, 0, 0, 0, W, 0, 0),
            (0, 0, 0, 0, 0, W, 0, 0)
        )

        expected = (
            (0, 0, 0, 0, 0, W, 0, 0),
            (0, 0, 0, 0, 0, W, 0, 0),
            (0, 0, 0, B, B, W, 0, 0),
            (0, 0, W, W, W, W, 0, 0),
            (0, 0, B, W, B, W, 0, 0),
            (0, 0, 0, W, W, W, W, W),
            (0, 0, 0, 0, 0, W, 0, 0),
            (0, 0, 0, 0, 0, W, 0, 0)
        )

        actual = moves.move(state, player='W', position=moves.Position(2, 3))

        for row in actual:
            print(row)

        self.assertEqual(expected, actual)

    def test_column_sequences(self):
        expected = ((moves.Position(5, 4), moves.Position(5, 3), moves.Position(5, 2), moves.Position(5, 1),
                     moves.Position(5, 0)), (moves.Position(5, 6), moves.Position(5, 7)))

        actual = tuple(moves.column_sequences(moves.Position(x=5, y=5)))

        self.assertEqual(set(expected), set(actual))

    def test_column_sequences_corner(self):
        expected = ((moves.Position(0, 1), moves.Position(0, 2), moves.Position(0, 3), moves.Position(0, 4),
                     moves.Position(0, 5), moves.Position(0, 6), moves.Position(0, 7)), ())

        actual = moves.column_sequences(moves.Position(x=0, y=0))

        self.assertEqual(set(expected), set(actual))

    def test_row_sequences(self):
        expected = ((moves.Position(4, 5), moves.Position(3, 5), moves.Position(2, 5), moves.Position(1, 5),
                     moves.Position(0, 5)), (moves.Position(6, 5), moves.Position(7, 5)))

        actual = tuple(moves.row_sequences(moves.Position(x=5, y=5)))

        self.assertEqual(set(expected), set(actual))

    def test_row_sequences_corner(self):
        expected = ((moves.Position(1, 0), moves.Position(2, 0), moves.Position(3, 0),
                     moves.Position(4, 0), moves.Position(5, 0), moves.Position(6, 0), moves.Position(7, 0)), ())

        actual = moves.row_sequences(moves.Position(x=0, y=0))

        self.assertEqual(set(expected), set(actual))

    def test_diagonal_sequences(self):
        expected = (
            (moves.Position(6, 6), moves.Position(7, 7)),
            (moves.Position(4, 4), moves.Position(3, 3), moves.Position(2, 2), moves.Position(1, 1),
             moves.Position(0, 0)),
            (moves.Position(6, 4), moves.Position(7, 3)),
            (moves.Position(4, 6), moves.Position(3, 7))
        )

        actual = tuple(moves.diagonal_sequences(moves.Position(x=5, y=5)))

        self.assertEqual(set(expected), set(actual))
