x = 1
hardcode = int(277678) #provided by problem set
#find exponent closest to value
while x**2 < hardcode:
    x += 2

# find nearest exponent
y = x**2
z = (x+2)**2

if abs(hardcode-y) <= abs(hardcode-z):
    cornerRow = x
else:
    cornerRow = x + 1

cornerDistance = cornerRow - abs(hardcode-cornerRow**2) - 1

print(cornerDistance)
