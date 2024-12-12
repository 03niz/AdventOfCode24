#ADVENT OF CYBER 2024#
####### DAY 02 #######
####### BY NIZ #######

def part1():

    # Opens and reads each line
    with open('input.txt', 'r') as file:
       
        for line in file:

            sequence = []
            diffSequence = []

            sequence = line.split()

            for i in range(1, len(sequence)):
                diff = 0
                diff = (int((sequence[i])) - int((sequence[i - 1])))
                diffSequence.append(diff)
            print(diffSequence)
                

def main():
    part1()

main()