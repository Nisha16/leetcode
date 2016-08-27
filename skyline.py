import heapq

def getSkyline(buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    
    idx, n = 0, len(buildings)
    liveBuildings, skyline = [], []
    while idx < n or len(liveBuildings) > 0:
        if len(liveBuildings) == 0 or (idx < n and buildings[idx][0] <= -liveBuildings[0][1]):
            start = buildings[idx][0]
            while idx < n and buildings[idx][0] == start:
                heapq.heappush(liveBuildings, [-buildings[idx][2], -buildings[idx][1]])
                #print "----- ", -buildings[idx][1]]
                idx += 1
        else:
            start = -liveBuildings[0][1]
            while len(liveBuildings) > 0 and -liveBuildings[0][1] <= start:
                heapq.heappop(liveBuildings)
        height = len(liveBuildings) and -liveBuildings[0][0]
        #print -liveBuildings[0][0]
        if len(skyline) == 0 or skyline[-1][1] != height:
            skyline.append([start, height])
    return skyline

s = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]

print getSkyline(s)  




def getSkyline_rec(low, high, buildings):
    skyLineList = []

    if low > high:
        return skyLineList

    elif low == high:
        x1 = buildings[low][0]
        x2 = buildings[low][1]
        h = buildings[low][2]

        element1 = [x1, h]
        element2 = [x2, 0]
        skyLineList.append(element2)
        skyLineList.append([0, element1])

        print skyLineList 

    else:
        mid = (low + high) // 2
        skyLineList_lower = getSkyline_rec(low, mid, buildings)
        skyLineList_higher = getSkyline_rec(mid + 1, high, buildings)

        return mergeskylines(skyLineList_lower, skyLineList_higher)


def mergeskylines(skyLineList_lower, skyLineList_higher):
    
    h1, h2 = 0, 0
    skyLine_merged = []

    while True:
        if skyLineList_lower is None and skyLineList_higher is None:
            break

        stripe1 = skyLineList_lower[0]
        stripe2 = skyLineList_higher[0]
        merged_stripe = []

        if stripe1[0] < stripe2[0]:
            merged_stripe[0] = stripe1[0]
            merged_stripe[1] = stripe1[1]

            if stripe1[1] < h2:
                merged_stripe[1] = h2

            h1 = stripe1[1]
            skyLineList_lower.pop(0) 


s = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]

# print "start: " , s

# getSkyline(0, 4, s)

# print "end: ", s



                        