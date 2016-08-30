def threeSum(num, target):
    num.sort()
    result = []
    i = 0                       # For the first item
    while i < len(num) - 2:
        j = i + 1               # For the middle item
        k = len(num) - 1        # For the last item
        while j < k:
            if num[i]+ num[j] + num[j] > 0 or num[i]+ num[k]+ num[k]< 0:
                # num[k] >= any num[j], num[j] <= any num[k]
                # Impossible to find a answer in the future
                break
            if num[i]+ num[j]+num[k] == target:
                # Because the num is sorted, so the num[i] <= num[j] <= num[k]
                # And in every round, i or j/k is different from the previous
                # round. Therefore, the answer [num[i], num[j], num[k]] is new
                # and unique for the result set.

                result.append([num[i], num[j], num[k]])

                # Skip duplicate num[j-1] and num[k+1]
                j += 1
                while j < k+1 and num[j] == num[j-1]:   j += 1
                k -= 1
                while k > j-1 and num[k] == num[k+1]:   k -= 1
            elif num[i] + num[j]+ num[k]< target:
                #result.append([num[i], num[j], num[k]])
                # Skip duplicate num[j-1]
                j += 1
                while j < k+1 and num[j] == num[j-1]:   j += 1
            else:
                #result.append([num[i], num[j], num[k]])
                # Skip duplicate num[k+1]
                k -= 1
                while k > j-1 and num[k] == num[k+1]:   k -= 1

        # Skip duplicate num[i-1]
        i += 1
        while i < len(num)-1 and num[i] == num[i-1]:  i += 1

    return result

def threesumfunc(nums, target):
    nums.sort()
    n = len(nums)

    count, k = 0, 2
    while k < n:
        i, j = 0, k - 1
        while i < j:  # Two Pointers, linear time.
            if nums[i] + nums[j] + nums[k] >= target:
                j -= 1
            else:
                count += j - i
                i += 1
        k += 1
        
    return count                    

def threeSumClosest( num, target):
    num.sort()
    mindiff=100000
    res=0
    array = []
    for i in range(len(num)):
        left=i+1; right=len(num)-1
        while left<right:
            sum=num[i]+num[left]+num[right]
            diff=abs(sum-target)
            if diff<mindiff: 
                array.append([num[i],num[left],num[right]]) 
                mindiff=diff; 
                res=sum    
            if sum==target: return sum
            elif sum<target: left+=1
            else: right-=1
    return res, "array is", array[-1]    


number = [0, 1,-1, 2, 3, -4]

print 'threeSum: ', threeSum(number, 0)

print 'trial: ', threesumfunc(number, 3)

print "closeset: ", threeSumClosest(number, 7)



