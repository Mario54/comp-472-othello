import moves
from functools import reduce


def all_captured(seq, state):
    return len(seq) == sum([1 for pos in seq if state.get_tile(pos) == state.player])


def immune_tiles(state):
    """
    Counts the number of tiles that are immune (cannot be turned).
    """
    immune = set()

    for pos in moves.find_tiles(state):
        dependent_sequences = [
            moves.column_sequences(pos),
            moves.row_sequences(pos),
            [
                moves.diagonal_sequence(pos, x_inc=1, y_inc=1),
                moves.diagonal_sequence(pos, x_inc=-1, y_inc=-1)
            ],
            [
                moves.diagonal_sequence(pos, x_inc=1, y_inc=-1),
                moves.diagonal_sequence(pos, x_inc=-1, y_inc=1)
            ]
        ]

        is_immune = reduce(
            lambda acc, seqs: acc and reduce(lambda result, seq: result or all_captured(seq, state), seqs, False),
            dependent_sequences,
            True
        )

        if is_immune:
            immune.add(pos)

    return immune
