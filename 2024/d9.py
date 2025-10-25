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
    # Parse input
    spaces = [int(c) for i, c in enumerate(input) if i % 2 == 1]
    blocks = [int(c) for i, c in enumerate(input) if i % 2 == 0]
    
    # Build initial disk representation as a list
    disk = []
    for i, block_size in enumerate(blocks):
        # Add file blocks
        disk.extend([i] * block_size)
        # Add free space (if not the last file)
        if i < len(spaces):
            disk.extend([None] * spaces[i])  # None represents free space
    
    # Compact: move blocks from right to left
    left = 0
    right = len(disk) - 1
    
    while left < right:
        # Find next free space from left
        while left < right and disk[left] is not None:
            left += 1
        
        # Find next file block from right
        while left < right and disk[right] is None:
            right -= 1
        
        # Swap
        if left < right:
            disk[left] = disk[right]
            disk[right] = None
            left += 1
            right -= 1
    
    # Calculate checksum
    checksum = sum(i * file_id for i, file_id in enumerate(disk) if file_id is not None)
    print(checksum)

if __name__ == "__main__":
    with open("2024/d9.txt") as f:
        input_data = f.read().strip()
    main(input_data)

    main(sample_input)
