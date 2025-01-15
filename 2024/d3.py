import re


def d1():

    with open("d3-sample.txt") as f:
        data = f.read().strip()

    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    matches = re.finditer(pattern, data)

    rsum = 0
    for m in matches:
        a = int(m.group(1))
        b = int(m.group(2))
        rsum += a * b

    print(rsum)


def d2():

    with open("d3.txt") as f:
        data = f.read().strip()

    pattern = re.compile(r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)")
    matches = re.finditer(pattern, data)
    do_state = True
    rsum = 0
    for m in matches:
        command = m.group()
        if command == "do()":
            do_state = True

        elif command == "don't()":
            do_state = False

        else:
            if do_state:
                a = int(m.group(1))
                b = int(m.group(2))
                rsum += a * b

    print(rsum)


if __name__ == "__main__":
    d1()
    d2()
