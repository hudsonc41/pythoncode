##for i in range(len(tower_heights)):
##    if i < len(tower_heights) - 1:
##        if tower_heights[i] > tower_heights[i + 1]:
##            if len(towerbd) == 0:
##                print(enumerate(tower_heights[i]))
##                towerbd.append(tower_heights.index(tower_heights[i]))
##                print(tower_heights.index(tower_heights[i]))##
##            else:
##                if tower_heights[i] <= towerbd[-1]: #compares to most recent tower
##                    print(enumerate((tower_heights[i])))
##                    towerbd.append(tower_heights.index(tower_heights[i]))
##                    print(tower_heights.index(tower_heights[i]))##
##    else:
##        if tower_heights[i] > tower_heights[i - 1]:
##            towerbd.append(tower_heights.index(tower_heights[i]))
##            print(tower_heights.index(tower_heights[i]))##
##print(towerbd)

tower_heights = [1, 2, 4, 2, 0, 1, 3, 1, 2]
towerbd = {}  # storing the points before decrease

for index, height in enumerate(tower_heights):
    if index != (len(tower_heights) - 1):
        if height > tower_heights[index + 1]:
            if len(towerbd) == 0:
                print(index, height)
                towerbd[height] = index
            else:
                if (
                    height > tower_heights[index + 1]
                    and height > tower_heights[index - 1]
                ):  # compares to most recent tower
                    print(index, height)
                    towerbd[height] = index
    #
    else:
        if height > tower_heights[index - 1]:
            print(index, height)
            towerbd[height] = index


rain = []
for index, tower in enumerate(towerbd):
    waters = tower_heights[towerbd.index(tower) : towerbd[towerbd.index(tower) + 1]]
    totwater = 0
    for waters in water:
        totwater = totwater + waters
    rain.append(totwater)


print(sum(rain))
