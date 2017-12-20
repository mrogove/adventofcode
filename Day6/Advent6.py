with open("Advent6input.txt") as file:
    valbankList = [int(n) for n in file.read().strip().split()]

seenVals = [] #retained list

while valbankList not in seenVals:
    seenVals.append(valbankList[:])
    m = max(valbankList)
    x = valbankList.index(m)
    valbankList[x] = 0 #also reset to 0!
    while m: #inside the mainlist
        x=(x+1)%len(valbankList)
        valbankList[x]+=1
        m-=1 #I hope

#once the seenVals contains valbankList value, breaks loop:
print (len(seenVals))
#to get part 2, need to find how long between cycles.
#the duplicate state won't have its index overwritten;
    #can use index value of first instance:
print (len(seenVals)-seenVals.index(valbankList))
