import pandas as pd
line = 0
old_line = 0
increase = 0

data = pd.read_csv('puzzle_input.txt')
total_increases = data.rolling(3).sum()

df = pd.DataFrame(total_increases)

for index, row in df.iterrows():

    # do this if not NaN
    line = row[0].astype(int)
    if int(line) > int(old_line):
        increase = increase + 1
    old_line = line
print(increase)
