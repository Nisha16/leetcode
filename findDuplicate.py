class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicate_number = set()
        found = False
        duplicate = 0
        for num in nums:
            if num in duplicate_number:
                found = True
                return num
            if num not in duplicate_number:
                duplicate_number.add(num)
