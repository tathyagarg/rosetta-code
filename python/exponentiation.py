# https://rosettacode.org/wiki/Exponentiation_operator

class number:
    def __init__(self, val):
        self.val = val

    def __pow__(self, power):
        t = 1
        for i in range(power):
            t *= self.val

        return t

def main():
    print(number(2.2) ** 3)

if __name__ == '__main__':
    main()

