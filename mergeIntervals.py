def mergeInterval(intervals):    

    sorted_by_lower_bound = sorted(intervals, key=lambda tup: tup[0])
    merged = []

    for higher in sorted_by_lower_bound:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            # test for intersection between lower and higher:
            # we know via sorting that lower[0] <= higher[0]
            if higher[0] <= lower[1]:
                upper_bound = max(lower[1], higher[1])
                merged[-1] = (lower[0], upper_bound)  # replace by merged interval
            else:
                merged.append(higher)
    return merged    



intervals = [(1,3),(2,6),(8,10),(5,9), (15,18)]

#intervals = [(0, 3), (1, 2)]

#inetrvals = [(6,8), (1,9), (2,4), (4,7)] 

print mergeInterval(intervals)

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        
        if len(intervals) == 0:
            return res
            
        #sort list according to the start value
        intervals.sort(key=lambda x:x.start)
        
        res.append(intervals[0])
        #scan the list
        for i in xrange(1,len(intervals)):
            cur = intervals[i]
            pre = res[-1]
            #check if current interval intersects with previous one
            if cur.start <= pre.end:
                res[-1].end = max(pre.end, cur.end) #merge
            else:
                res.append(cur)
        
        return res 





