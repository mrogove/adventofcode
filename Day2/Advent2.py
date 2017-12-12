import itertools

results = []
with open("Advent2input.txt") as inputfile:
    for line in inputfile:
        results.append(line.strip().split('\t'))

checksum = 0
sumdivs = 0

for array in results: #for each list in the list of lists
    array = list(map(int, array)) #change all to int
    checksum += (max(array) - min(array))
#now, still in each array in larger array, run all combinations
    for a,b in itertools.combinations(sorted(array),2):
        if b%a == 0:
            sumdivs += b//a

print(checksum) #part1
print(sumdivs)
