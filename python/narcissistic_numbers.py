def check_narcissistic(n: int) -> bool:
    return sum(map(lambda i: int(i) ** len(str(n)), str(n))) == n

def generate_narcissists(n: int):
    items = []
    i = 0
    while len(items) != n:
        if check_narcissistic(i): items.append(i)
        i += 1

    return items

def main():
    print(generate_narcissists(15))

if __name__ == '__main__':
    main()

