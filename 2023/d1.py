def read_input():
    with open("2023/d1.txt") as f:
        return f.readlines()


def p1():
    lines = read_input()
    running_sum = 0
    for line in lines:
        n1, n2 = 0, 0
        for c in line:
            if c.isdigit():
                n1 = int(c)
                break

        for c in line[::-1]:
            if c.isdigit():
                n2 = int(c)
                break

        running_sum += n1 * 10 + n2

    print(running_sum)


def p2():
    lines = read_input()
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    running_sum = 0
    vals = []
    for line in lines:
        line = line.strip()
        v = []
        running_str = ""
        for c in line:
            if c.isdigit():
                v.append(int(c))
                running_str = ""
            else:
                running_str += c
                if running_str in numbers:
                    v.append(numbers.index(running_str) + 1)
                    running_str = c
                else:
                    for num in numbers:
                        if running_str == num[: len(running_str)]:
                            break
                    else:
                        running_str = running_str[1:]
        s = v[0] * 10 + v[-1]
        running_sum += s
    print(running_sum)


if __name__ == "__main__":
    p1()
    p2()
