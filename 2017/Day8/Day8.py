#adapted from /user/pedrosorio
from collections import defaultdict #wanna use dicts

lines = open('Day8input.txt').read().splitlines() #simple read into array
registers = defaultdict(int) #define dictionary
maxval = 0 #init maxval
for line in lines:
#register, +/-, an int to change by, "if", other register, other operator, other int.
    reg1, inst, num, iff, reg2, op, num2 = line.split()
    if eval("registers[reg2] " + op + num2): #dicey - evaluating dict value. if variable passes "if...""
        if inst == 'inc':
            registers[reg1] += int(num) #perform operation
            if registers[reg1] > maxval: #keep track of maxvals for pt2
                maxval = registers[reg1]
        else:
            registers[reg1] -= int(num)

print ("Part 1:     ", max(registers.values()) )
print ("Part 2:     ", maxval)
