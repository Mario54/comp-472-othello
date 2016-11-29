import algorithms
import othello

from othello import B, W


def simple_draw_board(state):
    print('-------------------------------------------------')

    for row in state:

        print('|', end='')

        for item in row:
            print(str(' ' if item == 0 else str(item)).center(5), end='|')

        print()
        print('-------------------------------------------------')


class InteractiveGame(othello.BaseGame):
    def draw_board(self, possible_moves):
        state_copy = [list(row) for row in self.state.board]

        print(B + ' tiles: ' + str(othello.count_tiles(self.state, B)))
        print(W + ' tiles: ' + str(othello.count_tiles(self.state, W)))
        print()
        print('Current player: ' + self.state.player)
        print()

        for i, move in enumerate(possible_moves):
            state_copy[move.position.y][move.position.x] = str(i+1)

        simple_draw_board(state_copy)
        print()

    def input(self, possible_moves):
        if self.state.player == B:
            choice = algorithms.minimax_mario(possible_moves, self.state)

            print('The AI picked move #{}'.format(choice))

            return choice

        return int(input('Where would {} like to move? '.format(self.state.player)))

    def announce_winner(self):
        print()
        print('GAME OVER')
        simple_draw_board(self.state.board)
        print()
        if othello.determine_winner(self.state) is not None:
            print('Winner is ' + othello.determine_winner(self.state))
        else:
            print('It\'s a TIE!')
        print()

    def before_move(self):
        return '\n' * 5


if __name__ == '__main__':
    othello.run(InteractiveGame())
