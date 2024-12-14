inputList = []

with open('Q2\input.txt', 'r') as f:
    
    for line in f:
        
        entry = line.strip().split('\n')
        inputList.append(entry)

print(inputList)