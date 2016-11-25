import algorithms
from othello import B, W
from interactive_game import simple_draw_board

import othello


def white_algorithm(state, possible_moves):
    return algorithms.minimax_hilary(possible_moves, state)


def black_algorithm(state, moves):
    return algorithms.maximize_reversals(moves)
    # return algorithms.minimax_mario(moves, state)


class AutomaticGame(othello.BaseGame):
    def draw_board(self, possible_moves):
        print(self.state.player, end=' ')
        print('( ', end='')

        for row in self.state.board:
            print('( ', end='')
            for tile in row:
                if str(tile) != '0':
                    print(tile, end='')
                else:
                    print(' ', end='')

                print(' ', end='')

            print('), ', end='')

        print()

    def input(self, possible_moves):
        if self.state.player == B:
            choice = black_algorithm(self.state, possible_moves)
        else:
            choice = white_algorithm(self.state, possible_moves)

        return choice

    def announce_winner(self):
        self.draw_board(None)
        print()
        print('GAME OVER')
        simple_draw_board(self.state.board)
        print()
        if othello.determine_winner(self.state) != None:
            print('Winner is ' + othello.determine_winner(self.state))
        else:
            print('It\'s a TIE!')
        print()
        print('Black tiles: ' + str(othello.count_tiles(self.state, B)))
        print('White tiles: ' + str(othello.count_tiles(self.state, W)))


if __name__ == '__main__':
    othello.run(AutomaticGame())
