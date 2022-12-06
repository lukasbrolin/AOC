import numpy as np

INPUT_FILE = 'input.txt'

def findCalories():
    calories = []
    currentVal = 0
    with open(INPUT_FILE, 'r') as f:
                for line in f:
                    if line == '\n':
                        calories.append(currentVal)
                        currentVal = 0
                        continue
                    currentVal += int(line)

    return(calories)

def findMaxCalories():
    return(max(findCalories()))

print(findMaxCalories())

def takeTopThree(calories):
    return sum((np.sort(calories))[::-1][:3])

print(takeTopThree(findCalories()))
