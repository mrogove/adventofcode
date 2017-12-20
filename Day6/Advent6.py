with open("Advent6input.txt") as file:
    valbankList = [int(n) for n in file.read().strip().split()]

seenVals = [] #retained list

while valbankList not in seenVals:
    seenVals.append(valbankList[:])
    m = max(valbankList)
    x = valbankList.index(m)
    valbankList[x] = 0 #also reset to 0!
    while m:
        x=(x+1)%len(valbankList)
        valbankList[x]+=1
        m-=1 #I hope

print (len(seenVals))
