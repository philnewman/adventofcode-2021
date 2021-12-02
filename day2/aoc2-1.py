import re
input_file = open('puzzle_input.txt')
horiz = 0
depth = 0

lines = input_file.readlines()
for move in lines:
    chunks = re.split(' ',move)
    if chunks[0] == "up":
        depth = depth - int(chunks[1])
    if chunks[0] == "down":
        depth = depth + int(chunks[1])
    if chunks[0] == "forward":
        horiz = horiz + int(chunks[1])
print(horiz * depth)
