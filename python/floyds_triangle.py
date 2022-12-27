# https://rosettacode.org/wiki/Floyd's_triangle

def make_triangle(rows: int):
    final_num_size, v = len(str(int(rows * ((rows + 1)/2)))), 0
    for i in range(1, rows+1):
        for j in range(i):
            print(f'{(v := v + 1):{final_num_size}}', end=' ')
        print()

def main():
    make_triangle(14)

if __name__ == '__main__':
    main()
