with open('Advent9input.txt') as input_file:
    textline = input_file.readline() #no further parsing necessary

score = 0
current_depth = 0
#init flags; assumes first char fine
inside_garbage = False
skip_char = False
for char in textline:
    if inside_garbage == True:
        if skip_char == True:
            skip_char = False
        elif char == "!":
            skip_char = True
        elif char == ">":
            inside_garbage = False
    else:  # when inside group, not garbage
        if char == "{": #add to depth inside bracket
            current_depth += 1
        elif char == "}":
            score += current_depth
            current_depth -= 1
        elif char == "<":
            inside_garbage = True

print("Part 1:   ", score)
