from pathlib import Path

from tqdm import tqdm

day_9_input = Path("data/inputs/day_9/input.txt").read_text().strip()

# day_9_input = "2333133121414131402"

print(day_9_input[:20])

file_sizes = day_9_input[::2]
empty_sizes = day_9_input[1::2] + "0"

print(len(file_sizes), file_sizes[:10])
print(len(empty_sizes), empty_sizes[:10])

filesystem = []
for i, (file_size, empty_size) in enumerate(zip(file_sizes, empty_sizes)):
    for j in range(int(file_size)):
        filesystem.append(i)
    for j in range(int(empty_size)):
        filesystem.append(None)

print(filesystem[:20])


def remove_none_at_the_end(filesystem):
    while filesystem[-1] is None:
        filesystem.pop()
    return filesystem


for i, v in enumerate(filesystem):
    try:
        if v is None:
            filesystem = remove_none_at_the_end(filesystem)
            filesystem[i] = filesystem.pop()
    except IndexError:
        break
print(filesystem[:20])

filesystem = remove_none_at_the_end(filesystem)

checksum = 0
for i, v in enumerate(filesystem):
    checksum += i * v

print(checksum)
