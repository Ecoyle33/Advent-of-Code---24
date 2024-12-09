#Create two lists, each list contains one column from input.txt

list1 = []
list2 = []

with open('input.txt', 'r') as f:
    for line in f:
        entry1, entry2 = line.strip().split()
        list1.append(entry1)
        list2.append(entry2)

print(f'{list1}')
print(f'{list2}')