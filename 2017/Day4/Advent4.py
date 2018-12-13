import itertools

results = []
with open("Advent4input.txt") as inputfile:
    for line in inputfile:
        results.append(line.strip().split(' '))

validsum = 0
noanagram = 0

for array in results: #for each list in the list of lists
    if len(array) == len(set(array)):
        validsum += 1

#for each array: for each word, use #sorted# to alphebatize each string
    #then, use "".join to join each alphebatized string together
    #then, take the set of these; compare set of each array with each array
    if (len(array) == len(set(["".join(sorted(word)) for word in array]))):
        noanagram += 1

print(validsum) #part1
print(noanagram) #part2
