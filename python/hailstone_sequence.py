# https://rosettacode.org/wiki/Hailstone_sequence

def hailstone(start: int):
    n = start
    yield n
    while n != 1:
        n = [n//2, (3 * n) + 1][n % 2]
        yield n
    return 0

def main():
    print(*hailstone(12), sep=' -> ')

if __name__ == '__main__':
    main()
