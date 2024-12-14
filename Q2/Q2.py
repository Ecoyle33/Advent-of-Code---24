import numpy as np

inputList = []

with open('Q2\input.txt', 'r') as f:
    
    for line in f:
        
        entry = line.strip().split()
        entry = [int(x) for x in entry]
        inputList.append(entry)

numSafeLists = 0

for array in inputList:

    # Check if the lists elements are all increasing or decreasing
    
    for i in range(len(array) - 1):
        
        value1 = array[i]
        value2 = array[i + 1]

        diff = abs(value2 - value1)

        if ((diff > 0) and (diff <= 3)):
            numSafeLists += 1
        
        break

print(numSafeLists)      