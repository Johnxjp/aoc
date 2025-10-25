"""
Solving this

1. We know the number of spaces and the number of blocks
given by input string. They alternate.

We can get the number of spaces. 
Then we can work backwards from non-spaces and fill in.
we could keep track with a couple of pointers:

1. Keep track of spaces we are tracking
2. Keep track of numbers from the back
3. Stop when they overlap

Algorithm:
1. Start filling a string.
Move pointer left to right (i). if pointer % 2 == 1, then we have spaces
work from the back of the string. We have another pointer (j). That
jumps to numbers.

2. if j < i, then we just add remaining spaces to the end

3. We do check sum

"""

sample_input = "233313312141413140212"


def main(input: str) -> None:
    ordered_string = ""
    spaces = [int(c) for i, c in enumerate(input) if i % 2 == 1]
    blocks = [int(c) for i, c in enumerate(input) if i % 2 == 0]
    remaining = [(spaces * str(id)) for id, spaces  in enumerate(blocks)]
    # print(input, spaces, blocks, remaining)
    space_index = 0
    blocks_i = 0
    remaining_index = len(remaining) - 1

    while blocks_i < remaining_index:
        ordered_string += blocks[blocks_i] * str(blocks_i)
        remaining_spaces = spaces[space_index]
        
        # Fill in spaces
        while remaining_spaces > 0 and blocks_i < remaining_index:
            r = remaining[remaining_index]
            blocks_available = len(r)
            # print(remaining_index, blocks_available, remaining_spaces)
            if blocks_available > remaining_spaces:
                bits = r[:remaining_spaces]
                ordered_string += bits
                remaining[remaining_index] = r[remaining_spaces:]
            else:
                ordered_string += r
                remaining[remaining_index] = ""
                remaining_index -= 1

            remaining_spaces -= blocks_available

        blocks_i += 1
        space_index += 1

    if len(remaining[remaining_index]) > 0:
        ordered_string += remaining[remaining_index]

    for s in spaces:
        ordered_string += s * "."


    # print(ordered_string)
    final_output = sum(i * int(c) for i, c in enumerate(ordered_string) if c != ".")
    print(final_output)


if __name__ == "__main__":
    with open("2024/d9.txt") as f:
        input_data = f.read().strip()
    main(input_data)

    main(sample_input)
