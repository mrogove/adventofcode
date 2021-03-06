#used coordinate tips from: https://www.redblobgames.com/grids/hexagons/
#define three coordinate planes: x,y,z
#cube distance defined as:
#   function cube_distance(a, b):
#    return (abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)) / 2
#in our case, b is the origin, or (0,0,0)

i = open("Advent11input.txt", "r")
steps = i.read().strip().split(",")

x = 0
y = 0
z = 0

distances = [] # list for tracking max distances in part 2

for step in steps:
    if step == "n":
        x += 1
        z -= 1
    elif step == "s":
        z += 1
        x -= 1
    elif step == "ne":
        x += 1
        y -= 1
    elif step == "nw":
        y += 1
        z -= 1
    elif step == "se":
        z += 1
        y -= 1
    elif step == "sw":
        y += 1
        x -= 1
    distances.append(int((abs(x) + abs(y) + abs(z))/ 2))

print (int((abs(x) + abs(y) + abs(z))/ 2)) #won't accept float.
print (max(distances))
