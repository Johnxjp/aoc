import re


def d1():

    with open("d3.txt") as f:
        data = f.read().strip()

    pattern = re.compile(r"(mul\((\d+),(\d+)\))")
    matches = re.findall(pattern, data)

    rsum = 0
    for m in matches:
        a = int(m[1])
        b = int(m[2])
        rsum += a * b

    print(rsum)


if __name__ == "__main__":
    d1()
