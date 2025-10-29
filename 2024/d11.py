from collections import defaultdict

def naive(input: str, nblinks: int):
    data = input.split()
    new_data = []
    for _ in range(nblinks):
        for i in data:
            if i == "0":
                new_data.append("1")
            elif (n := len(i)) % 2 == 0:
                mid = n // 2
                first, second = i[:mid], i[mid:]
                second = str(int(second))
                new_data.append(first)
                new_data.append(second)
            else:
                new_data.append(str(int(i) * 2024))

        data = new_data
        new_data = []
    return len(data)


def smarter(input: str, nblinks: int):

    data = {}
    for value in input.split():
        data[value] = data.get(value, 0) + 1

    for _ in range(nblinks):
        new_data = defaultdict(int)
        for value, count in data.items():
            if value == "0":
                new_data["1"] += count

            elif (n := len(value)) % 2 == 0:
                mid = n // 2
                first, second = value[:mid], value[mid:]
                second = str(int(second))
                new_data[first] += count
                new_data[second] += count
            else:
                new_value = str(int(value) * 2024)
                new_data[new_value] += count

        data = new_data

    total_count = sum(data.values())
    return total_count


if __name__ == "__main__":

    sample = "125 17"
    sample_2 = "0 1 10 99 999"
    input = "28591 78 0 3159881 4254 524155 598 1"
    print(smarter(sample, 25))
    print(smarter(sample_2, 25))
    print(smarter(input, 25))
    
    # day 2
    print(smarter(input, 75))
