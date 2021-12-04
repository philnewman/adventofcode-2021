import numpy as np

def get_input():
    with open('puzzle_input.txt') as f:
        return [list(map(int, list(l))) for l in f.read().splitlines()]

def determine_column(target):
    bits = []
    for x in range(len(numbers[0])):
        one_count  = np.count_nonzero(numbers[:,x] == 1)
        zero_count = np.count_nonzero(numbers[:,x] == 0)
        if (one_count > zero_count):
            bits.append(target)
        else:
            bits.append(1-target)
    number = "".join([str(i) for i in bits])
    number_dec = int(number,2)
    return number_dec

numbers = np.array(get_input())
gamma = determine_column(1);
epsilon = determine_column(0);
answer = gamma * epsilon

print("Power Consumption: ",answer)
