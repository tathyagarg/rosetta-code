# https://rosettacode.org/wiki/Department_numbers

import itertools

def make_sanitation_fire() -> list[tuple[int, int]]:
    sanitation_fire = list(itertools.product(range(1, 8), range(1, 8)))

def department_numbers():
    print(f'--police-- --sanitation-- --fire--')
    for police in range(2, 8, 2):
        curr = list(filter(lambda tup: sum(tup) + police == 12 and tup[0] != tup[1] and tup[1] != police and police != tup[0], sanitation_fire))
        for s, f in curr:
            print(f'{police:^ 10}\t{s:< 14}\t{f}')

def main():
    department_numbers()

if __name__ == "__main__":
    main()
