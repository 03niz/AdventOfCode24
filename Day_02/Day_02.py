#ADVENT OF CYBER 2024#
####### DAY 02 #######
####### BY NIZ #######

def part1():

    # Opens and reads each line
    with open('input.txt', 'r') as file:
        unsafe = 0
       
        for line in file:

            sequence = []
            diffSequence = []
            harmony = ""


            sequence = line.split()

            for i in range(1, len(sequence)):
                diff = 0
                diff = (int((sequence[i])) - int((sequence[i - 1])))
                diffSequence.append(diff)
            
            if int(diffSequence[0]) < 0:
                polaritySet = "negaitve"
            
            if int(diffSequence[0]) >= 0:
                polaritySet = "positve"

            for i in range(len(diffSequence)):

                polarity = ""
                polaritySet = ""
                
                if int(diffSequence[i]) < 0:
                    polaritySet = "negaitve"
            
                if int(diffSequence[i]) > 0:
                    polaritySet = "positve"
                
                if polarity != polaritySet:
                    harmony = "broken"
            
            if harmony == "broken":
                unsafe = unsafe + 1
            print(diffSequence)

    
    print(unsafe)




part1()
