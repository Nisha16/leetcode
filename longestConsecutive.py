class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, consecutive = 1, {key: 0 for key in nums}
        for i in nums:
            if consecutive[i] == 0:
                consecutive[i] = 1
                left, right = consecutive.get(i - 1, 0), consecutive.get(i + 1, 0)
                length = 1 + left + right
                result, consecutive[i - left], consecutive[i + right] = max(result, length), length, length
        return result 
