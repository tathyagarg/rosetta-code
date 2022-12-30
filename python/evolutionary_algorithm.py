import random
import string

def fitness(targ: str, comp: str) -> float:
    return sum(x == y for x, y in zip(targ, comp)) - len(targ)

def mutate(text: str) -> str:
    chars = 3
    indicies = random.sample(range(len(text)), k=chars)
    copy = [*text]

    for ind in indicies:
        copy[ind] = random.choice(string.ascii_uppercase + " ")

    return "".join(copy)

def generate_random_text(length: int):
    return "".join(random.choices(string.ascii_uppercase + " ", k=length))

def evolve(targ: str, par: str, C: int = 4) -> int:
    iterations = 0

    fitness_score = fitness(targ, par)
    while fitness_score != 0:
        iterations += 1

        copies = [mutate(par) for _ in range(C)] + [par]
        par = max(copies, key=lambda i: fitness(targ, i))
        fitness_score = fitness(targ, par)

    return iterations

def run_tests(text: str, generations: int) -> tuple[float, int, int]:
    tests = [0]*generations
    for i in range(generations):
        v = evolve(text, generate_random_text(len(text)), 1_000)
        tests[i] = v
        print(f'Test {i+1} completed - {v} generations')

    return sum(tests)/generations, min(tests), max(tests)

def main():
    target = "METHINKS IT IS LIKE A WEASEL"
    avg, minimum, maximum = run_tests(target, 150)
    print(f'{avg = }, {minimum = }, {maximum = }')

if __name__ == '__main__':
    main()
