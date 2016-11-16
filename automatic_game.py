from algorithms import maximize_reversals
from othello import B
from interactive_game import simple_draw_board

import othello


def white_algorithm(state, possible_moves):
    return maximize_reversals(possible_moves)


def black_algorithm(state, moves):
    return 1


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
            choice = black_algorithm(self.state, possible_moves)
        else:
            choice = white_algorithm(self.state, possible_moves)

        return choice

    def announce_winner(self):
        print()
        print('GAME OVER')
        simple_draw_board(self.state)
        print()
        print('Winner is ' + othello.determine_winner(self.state))


if __name__ == '__main__':
    othello.run(AutomaticGame())
