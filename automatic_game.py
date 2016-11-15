from algorithms import maximize_reversals
from orthello import B

import orthello


def white_algorithm(state, possible_moves):
    return maximize_reversals(possible_moves)


def black_algorithm(state, moves):
    return 1


class AutomaticGame(orthello.BaseGame):
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
            choice = black_algorithm(self.state, possible_moves)
        else:
            choice = white_algorithm(self.state, possible_moves)

        return choice

    def announce_winner(self):
        print()
        print('GAME OVER')
        self.draw_board(None)
        print()
        print('Winner is ' + orthello.determine_winner(self.state))


if __name__ == '__main__':
    orthello.run(AutomaticGame())
