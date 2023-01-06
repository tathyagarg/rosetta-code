# https://rosettacode.org/wiki/Numbers_with_equal_rises_and_falls

def in_sequence(n: int) -> bool:
    n = str(n)
    rises, falls = 0, 0
    for i, char in enumerate(n[:-1]):
        if int(n[i]) < int(n[i + 1]):
            rises += 1
        elif int(n[i]) > int(n[i + 1]):
            falls += 1

    return rises == falls

def generate_numbers(limit: int):
    curr = 0
    found = 0
    while found != limit:
        if in_sequence(curr):
            found += 1
            yield curr
        curr += 1

def main():
    index = 0
    limit = 10_000_000

    for i in generate_numbers(limit + 1):
        if index < 200:
            print(i, end=[f'{" "*(4-len(str(i)))} ', '\n'][index % 10 == 9])
        index += 1
    print(f'{limit:,}th number is: {i:,}')

if __name__ == '__main__':
    main()

