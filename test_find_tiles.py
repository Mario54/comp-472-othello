from unittest import TestCase

import moves


class TestFindTiles(TestCase):
    def test_find_tiles_white(self):
        state = (
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 'W', 'B', 0, 0, 0),
            (0, 0, 0, 'B', 'W', 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0)
        )

        expected = ((3, 3), (4, 4))

        actual = moves.find_tiles(state, player='W')

        self.assertEqual(set(expected), set(actual))

    def test_find_tiles_black(self):
        state = (
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 'W', 'B', 0, 0, 0),
            (0, 0, 0, 'B', 'W', 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0)
        )

        expected = ((4, 3), (3, 4))

        actual = moves.find_tiles(state, player='B')

        self.assertEqual(set(expected), set(actual))

    def test_find_tiles_edge(self):
        state = (
            ('B', 0, 0, 0, 0, 0, 0, 'B'),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 'W', 'B', 0, 0, 0),
            (0, 0, 0, 'B', 'W', 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
            ('B', 0, 0, 0, 0, 0, 0, 'B')
        )

        expected = ((4, 3), (3, 4), (0, 0), (7, 0), (0, 7), (7, 7))

        actual = moves.find_tiles(state, player='B')

        self.assertEqual(set(expected), set(actual))
