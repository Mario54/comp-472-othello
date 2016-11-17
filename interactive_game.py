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
        state_copy = [list(row) for row in self.state]

        print('Black tiles: ' + str(othello.count_tiles(self.state, B)))
        print('White tiles: ' + str(othello.count_tiles(self.state, W)))
        print()
        print('Current player: ' + self.player)
        print()
        for i, move in enumerate(possible_moves):
            state_copy[move.position.y][move.position.x] = i + 1

        simple_draw_board(state_copy)
        print()

    def input(self, possible_moves):
        if self.player == B:
            choice = algorithms.minimax_mario(possible_moves, self.state, self.player)

            print('The AI picked move #{}'.format(choice))

            return choice

        return int(input('Where would {} like to move? '.format(self.player)))

    def announce_winner(self):
        print()
        print('GAME OVER')
        simple_draw_board(self.state)
        print()
        print('Winner is ' + othello.determine_winner(self.state))

    def before_move(self):
        return '\n' * 5


if __name__ == '__main__':
    othello.run(InteractiveGame())
