class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 0
        index2 = len(numbers)-1
        found = False
        result = []
        while not index1 == index2 and found == False:
            if numbers[index1] + numbers[index2] == target:
                found = True
                result.append(index1+1)
                result.append(index2+1)
            elif numbers[index1] + numbers[index2] > target:
                index2 -= 1
            elif numbers[index1] + numbers[index2] < target:
                index1 += 1
        return result 