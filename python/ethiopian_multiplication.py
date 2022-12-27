# https://rosettacode.org/wiki/Ethiopian_multiplication

def make_left_column(n: int) -> list[int]:
    yield n
    while n != 1:
        n //= 2
        yield n

def make_right_column(n: int, col_size: int) -> list[int]:
    for i in range(1, col_size+1):
        yield n
        n *= 2

def do_multiplaction(x: int, y: int) -> int:
    left_col = list(make_left_column(x))
    right_col = list(make_right_column(y, len(left_col)))

    table = {i: j for i, j in zip(left_col, right_col) if i % 2 != 0}
    return sum(table.values())

def main():
    print(do_multiplaction(17, 34))

if __name__ == '__main__':
    main()
