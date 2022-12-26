# https://rosettacode.org/wiki/21_game
import random

def take_input():
    while True:
        try:
            inp = int(input('Enter your choice:\n1. Play 1\n2. Play 2\n3. Play 3\n4. Quit\n5. Restart\n->'))
            if not 0 <= inp <= 5:
                raise ArithmeticError
            if inp == 4:
                quit()
        except ValueError:
            print("Invalid input! Your input has to be a number!")
        except ArithmeticError:
            print("Invalid input! Your input has to be between 1 and 5!")
        else:
            return inp

def game():
    total = 0

    while not total > 21:
        print(f'Score: {total}')
        user_inp = take_input()
        if user_inp == 5:
            total = 0
            print("Restarted!\n" + "="*15)
            continue
        total += user_inp

        if total == 21: return 1
        if total > 21: return -1

        computer = random.randint(1, 3)
        print(f"Computer chose: {computer}")
        total += computer

        if total == 21: return 2
        if total > 21: return -2
    return 0

def main():
    text_map = {
        1: "You win!",
        -1: "You lost.. Your addition made the total go above 21...",
        2: "You lost.. The computer reached 21 first...",
        -2: "You win! The computer made the total go above 21!",
        0: "Draw!"
    }

    winner = game()
    print(text_map[winner])

if __name__ == '__main__':
    main()
