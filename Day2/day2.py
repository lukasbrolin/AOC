import numpy as np
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

INPUT_FILE = 'input.txt'

def findScore():
    score = 0
    with open(INPUT_FILE, 'r') as f:
                for line in f:
                    round = line.strip('\n').split(' ')
                    score += valuateRound(transform(round[0]),transform(round[1]))
    return(score)

def transform(value):
    match value:
        case 'A' | 'X':
            return RPS.ROCK
        case 'B' | 'Y':
            return RPS.PAPER
        case 'C' | 'Z':
            return RPS.SCISSORS

def valuateRound(valueOpp, valueMe):
    if(valueOpp==valueMe):return valueMe.value+3
    match (valueOpp, valueMe):
        case RPS.ROCK,RPS.PAPER:
            return 8
        case RPS.PAPER,RPS.SCISSORS:
            return 9
        case RPS.SCISSORS,RPS.ROCK:
            return 7
        case default:
            return valueMe.value

print(findScore())

def findResult():
    score = 0
    with open(INPUT_FILE, 'r') as f:
                for line in f:
                    round = line.strip('\n').split(' ')
                    score += valuateRound(transform(round[0]),cheat(transform(round[0]),round[1]))
    return(score)

def cheat(valueOpp,result):
    match (result):
        case 'Y':
            return valueOpp
        case 'X':
            if(valueOpp==RPS.PAPER):
                return RPS.ROCK
            elif(valueOpp==RPS.ROCK):
                return RPS.SCISSORS
            else:
                return RPS.PAPER
        case 'Z':
            if(valueOpp==RPS.PAPER):
                return RPS.SCISSORS
            elif(valueOpp==RPS.ROCK):
                return RPS.PAPER
            else:
                return RPS.ROCK
        
print(findResult())