from collections import OrderedDict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        temp = OrderedDict()
        for num in nums:
            try:
                temp[num] += 1
            except:
                temp[num] = 1
        temp = OrderedDict(sorted(temp.items(), key=lambda t: t[1], reverse=True))
        print temp
        output = []
        count = 0
        for key in temp:
            if count < k:
                print 'out: ', count
                output.append(key)
                count += 1
        return output