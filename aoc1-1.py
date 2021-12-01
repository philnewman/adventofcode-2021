input_file = open('puzzle_input.txt')
increase = 0
old_line = 0

lines = input_file.readlines()
for line in lines:
    if int(line) > int(old_line):
        increase = increase + 1
    old_line = line
input_file.close()
print(increase-1)
