# https://rosettacode.org/wiki/Forward_difference

def forward(items: list[int], *, times: int = 1, display_all: bool = False) -> list[int]:
    if times == 0:
        return items

    new = [0]*(len(items)-1)
    for i, item in enumerate(items[:-1]):
        new[i] = items[i+1] - item

    if display_all:
        print(new)
    return forward(new, times=times-1, display_all=display_all)

def main():
    forward([90, 47, 58, 29, 22, 32, 55, 5, 55, 73], times=9, display_all=True)

if __name__ == '__main__':
    main()
