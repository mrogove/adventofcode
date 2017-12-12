results = []
with open("Advent4input.txt") as inputfile:
    for line in inputfile:
        results.append(line.strip().split(' '))

validsum = 0

for array in results: #for each list in the list of lists
    if len(array) == len(set(array)):
        validsum += 1

print(validsum)
