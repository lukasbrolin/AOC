import numpy as np
from string import ascii_lowercase,ascii_uppercase
from collections import Counter

INPUT_FILE = 'input.txt'

def findCommon():
    sum = 0
    with open(INPUT_FILE, 'r') as f:
                for line in f:
                    firstpart, secondpart = Counter(line[:int(len(line)/2)]), Counter(line[int(len(line)/2):])
                    common = firstpart & secondpart
                    sum += findPrio(sorted(common.elements())[0])
    return(sum)

def findCommonBadge():
    sum = 0
    currentGroup = []
    i = 0
    with open(INPUT_FILE, 'r') as f:
                for line in f:
                    currentGroup.append(line.strip('\n'))
                    
                    if(i==2):
                        common = Counter(currentGroup[0]) & Counter(currentGroup[1]) & Counter(currentGroup[2])
                        sum += findPrio(sorted(common.elements())[0])
                        i=0
                        currentGroup = []
                        continue

                    i+=1
    return(sum)

def findPrio(char):
    if(char.islower()):
        return loop(ascii_lowercase,char,1)
    else:
        return loop(ascii_uppercase,char,27)

def loop(ascii,char,i):
    for ch in ascii:
        if(ch==char):
            return i
        i+=1

print(findCommonBadge())