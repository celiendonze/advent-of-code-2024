import re
from pathlib import Path

input_path = Path(__file__).parent.parent / "data/inputs/day_3/input.txt"

lines = input_path.read_text().split("\n")

mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
s = 0
for line in lines:
    if not line:
        continue
    matches = re.findall(mul_pattern, line)

    for match in matches:
        s += int(match[0]) * int(match[1])

print("sum of mul:")
print(s)

text = "".join(lines)
pattern = re.compile(r"(^|do\(\))(.*?)($|don't\(\))")
matches = re.findall(pattern, text)

s = 0
for match in matches:
    sub_text = match[1]
    mul_matches = re.findall(mul_pattern, sub_text)
    for mul_match in mul_matches:
        s += int(mul_match[0]) * int(mul_match[1])


# print(matches)
print("sum of mul (do and don't):")
print(s)
