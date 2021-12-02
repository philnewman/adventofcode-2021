input_file = open('puzzle_input.txt')
horiz = 0
depth = 0
aim = 0

lines = input_file.readlines()
for line in lines:
    d, n = line.split()
    n = int(n)
    if d == "up":
        aim -= n
    if d == "down":
        aim += n
    if d == "forward":
        horiz += n
        depth += n * aim
print(depth * horiz)
