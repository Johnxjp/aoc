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

sample_input = "2333133121414131402"


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
    
    print(disk)
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

def day2(input: str):
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

    i = len(disk) - 1
    while i > 0:
        if (fileid := disk[i]) is not None:
            block_size = blocks[fileid]
            # print(fileid, block_size)
            
            # Find spaces
            space_index_start = 0
            while space_index_start < len(disk):
                if disk[space_index_start] == fileid:
                    break

                if disk[space_index_start] is None:
                    space_size = 0
                    while (space_index_start + space_size) < len(disk) and disk[space_index_start + space_size] is None:
                        space_size += 1
                    # print(fileid, space_index_start, space_index_start + space_size)
                    if space_size >= block_size:
                        for j in range(space_index_start, space_index_start + block_size):
                             disk[j] = fileid
                        
                        for j in range(i - block_size + 1, i + 1):
                            disk[j] = None
                        break

                    space_index_start += space_size

                else:
                    space_index_start += 1
            
            # Move pointer regardless of if can move block or not
            i -= block_size
        else:
            i -= 1
    
    checksum = sum(i * file_id for i, file_id in enumerate(disk) if file_id is not None)
    # print(disk)
    print(checksum)


if __name__ == "__main__":
    with open("2024/d9.txt") as f:
        input_data = f.read().strip()

    main(sample_input)
    main(input_data)
    day2(sample_input)
    day2(input_data)
