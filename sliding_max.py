import collections

def slidingMaximum(A, B):
    deque = collections.deque()
    result = []
    for i in range(len(A)):
        while deque and A[deque[-1]] <= A[i]:
            deque.pop()
        deque.append(i)
        
        if deque[0] == i - B: deque.popleft()
        if i >= B - 1: result.append(A[deque[0]])
    return result


A = [1,3,-1,-3,5,3,6,7]

print slidingMaximum(A, 3)    