def maximize_reversals(possible_moves):
    return possible_moves.index(max(possible_moves, key=lambda m: len(m.reversals))) + 1