from pathlib import Path

input_path = Path(__file__).parent.parent / "data/inputs/day_1/input.txt"

col1 = []
col2 = []
text = input_path.read_text()
for line in text.split("\n"):
    if line:
        ints = line.split("   ")
        col1.append(int(ints[0]))
        col2.append(int(ints[1]))

print("sum of distances:")
print(sum([abs(a - b) for a, b in zip(sorted(col1), sorted(col2))]))

print("similarity score:")
print(sum([a * col2.count(a) for a in col1]))
