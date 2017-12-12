i = 0
stepCount = 0
maze = [] #the challenge list

with open("Advent5input.txt") as inputfile:
    for line in inputfile:
        maze.append(int(line))

while i < len(maze):
    maze[i] += 1
    i = i + maze[i] - 1
    stepCount += 1

print(stepCount)
