import sys


def d1():
    filename = sys.argv[1]

    with open(filename) as f:
        data = f.read().splitlines()

    arrays = [line.split() for line in data]
    a, b = zip(*arrays)
    a = list(sorted(map(int, a)))
    b = list(sorted(map(int, b)))

    diff = 0
    for i in range(len(a)):
        diff += abs(a[i] - b[i])

    print(diff)


def d2():

    filename = sys.argv[1]
    a = []
    b = {}
    with open(filename) as f:
        for line in f:
            _a, _b = map(int, line.split())
            a.append(_a)
            b[_b] = b.get(_b, 0) + 1

    sim_score = 0
    for n in a:
        sim_score += n * b.get(n, 0)

    print(sim_score)


if __name__ == "__main__":
    d1()
    d2()
