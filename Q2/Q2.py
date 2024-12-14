inputList = []

with open('Q2\input.txt', 'r') as f:
    
    for line in f:
        
        entry = line.strip().split()

        entry = [int(x) for x in entry]

        inputList.append(entry)


