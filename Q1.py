#Create two lists, each list contains one column from input.txt
list1 = []
list2 = []

with open('input.txt', 'r') as f:
    for line in f:
        entry1, entry2 = line.strip().split()
        list1.append(entry1)
        list2.append(entry2)

list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

list1.sort()
list2.sort()

totalDist = 0

# Equal length, can choose either list for range
for i in range(len(list1)):
    element1 = list1[i]
    element2 = list2[i]

    dist = abs(element2 - element1)

    totalDist += dist

print(totalDist)