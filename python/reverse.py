# https://rosettacode.org/wiki/Reverse_a_string

def reverse(text: str) -> str:
    return text[::-1]

def main():
    print(reverse('abc'))
    print(reverse('kekw'))

if __name__ == '__main__':
    main()
