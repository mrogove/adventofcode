with open('C:/Users/mrogove/AdventOfCode/Advent1input.txt') as f:
    lines = f.read()
lines.replace(" ", "")

sumval = 0

for i in range(1,len(lines)):
    if lines[i] == lines[i-1]:
        sumval += int(lines[i-1])

if lines[0] == lines[-1]:
    sumval += int(lines[0])

print (sumval)
