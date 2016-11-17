import algorithms
from othello import B

import othello


def white_algorithm(state, player, possible_moves):
    return algorithms.minimax_mario(possible_moves, state, player)


def black_algorithm(state, player, moves):
    return algorithms.maximize_reversals(moves)


class AutomaticGame(othello.BaseGame):
    def draw_board(self, possible_moves):
        print(self.player, end=' ')
        print('( ', end='')

        for row in self.state:
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
        if self.player == B:
            choice = black_algorithm(self.state, self.player, possible_moves)
        else:
            choice = white_algorithm(self.state, self.player, possible_moves)

        return choice

    def announce_winner(self):
        print()
        print('GAME OVER')
        self.draw_board(None)
        print()
        print('Winner is ' + othello.determine_winner(self.state))


if __name__ == '__main__':
    othello.run(AutomaticGame())
