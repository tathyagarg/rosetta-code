# https://rosettacode.org/wiki/15_puzzle_game
import random

SOLVED_BOARD = [*range(1, 16)] + [0]

class Board:
    add_map = {
        'U': lambda i: -(i * 4),
        'D': lambda i: i * 4,
        'L': lambda i: -i,
        'R': lambda i: i
    }

    def __init__(self, *, debug=False):
        self.board: list[int] = random.sample(range(16), 16)
        if debug:
            self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15]
        self.move_count = 0

    def display(self):
        headers = 'ABCD'
        print(' ' * 4 + " | ".join(f' {c}  ' for c in headers))
        for i in range(4):
            print(f' {headers[i]} ', end='|')
            print(*map(lambda n: [' '*4, ' ' + str(n).ljust(3, ' ')][bool(n)], self.board[i * 4:(i + 1) * 4]), sep=' | ')
        print()

        return self

    @property
    def zero_location(self): return divmod(self.board.index(0), 4)[::-1]

    @property
    def is_solved(self): return self.board == SOLVED_BOARD

    def do_move(self):
        self.move_count += 1
        zero_x, zero_y = self.zero_location

        move = input('Enter move (U/D/L/R): ').upper()
        while move not in ['U', 'D', 'L', 'R'] or any([
            zero_y == 3 and move == 'U',
            zero_x == 3 and move == 'L',
            zero_y == 0 and move == 'D',
            zero_x == 0 and move == 'R'
        ]):
            move = input('Invalid! Enter move: U/D/L/R: ').upper()

        row_column = input('Enter row/column (A/B/C/D): ').upper()
        while row_column not in ['A', 'B', 'C', 'D'] or ('E' in 'ABCD'.replace(row_column, 'E') and (
            'ABCD'.index(row_column) == (zero_x if move in 'LR' else zero_y)
        )):
            row_column = input('Invalid! Enter row/column (A/B/C/D): ').upper()

        print()

        x, y = filter(lambda i: i >= 0, (zero_x if move not in 'LR' else -1,) + ('ABCD'.index(row_column),) + (zero_y if move in 'LR' else -1,))

        tiles_to_move = []
        for i in range(4):
            tile = (y * 4 + x) + Board.add_map[move](i)
            if self.board[tile] == 0:
                break
            tiles_to_move.append(tile)
        tiles_to_move[:] = tiles_to_move[::-1]

        for tile in tiles_to_move:
            index_0 = self.board.index(0)
            self.board[index_0], self.board[tile] = self.board[tile], self.board[index_0]

        self.display()
        return self

def main():
    board = Board().display()
    while not board.is_solved:
        board = board.do_move()
    print(f'You solved it in {board.move_count} moves!')

if __name__ == '__main__':
    main()
