def d1(input: str, nblinks: int):
    """

    If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
    The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone.
    (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.


    if you have a map of keys = values and values = indexes?
    or you could do array manipulation instead. Would require linear pass each time? What about tree

    'order is preserved' suggesting array is good.

    The number of stones is going to be huge and the array size massive.
    After 25 blinks "125 17" results in 55312 stones!

    How do you save memory? Where are the redundancies?
    You know that the array preserves order.
    If you're just counting stones then you don't need order just resulting numbers

    Three sets? You could use maps to reduce space
    zeros -> count
    evens -> number
    odds -> number

    Worst case len(keys) = len(list)

    Not asking for stone only number of stones so let's be smart. Order preserving means we
    just operate on starting. There's no intermingling and we apply operation on each unique starting number
    """
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


def d2(input: str, nblinks: int):

    data = {}
    for value in input.split():
        data[value] = data.get(value, 0) + 1

    for _ in range(nblinks):
        new_data = {}
        for value, count in data.items():
            if value == "0":
                new_data["1"] = new_data.get("1", 0) + count

            elif (n := len(value)) % 2 == 0:
                mid = n // 2
                first, second = value[:mid], value[mid:]
                second = str(int(second))
                new_data[first] = new_data.get(first, 0) + count
                new_data[second] = new_data.get(second, 0) + count
            else:
                new_value = str(int(value) * 2024)
                new_data[new_value] = new_data.get(new_value, 0) + count

        data = new_data

    total_count = sum(data.values())
    return total_count


if __name__ == "__main__":

    sample = "125 17"
    sample_2 = "0 1 10 99 999"
    input = "28591 78 0 3159881 4254 524155 598 1"

    print(d1(sample, 25))
    print(d1(sample_2, 25))
    print(d1(input, 25))
    # day 2
    print(d2(sample, 25))
    print(d2(sample_2, 25))
    print(d2(input, 25))
    print(d2(input, 75))
