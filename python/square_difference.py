# https://rosettacode.org/wiki/Find_square_difference

def check_condition(n: int) -> bool:
    return n ** 2 - (n - 1) ** 2 > 1000

def get_lowest() -> int:
    curr = 0
    while True:
        if check_condition(curr): return curr
        curr += 1
        print(curr)

def main():
    print(f"The lowest number satisfying the conditon is: {get_lowest()}")

if __name__ == "__main__":
    main()
