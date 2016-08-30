import heapq

def merge(arr):

	heap = [(l[0],i,0) for i,l in enumerate(arr) if len(l) > 0]

	print heap
	heapq.heapify(heap)

	lst = []

	while heap:
		item,lst_index,item_index = heapq.heappop(heap)
		print "item: ", item
		print 'last index: ' , lst_index
		print 'ite index: ', item_index
		lst.append(item)
		if item_index + 1 < len(arr[lst_index]):
			print "length: ", len(arr[lst_index])
			heapq.heappush(heap,(arr[lst_index][item_index+1],lst_index,item_index+1))
			print "H: ", heap

	if len(lst) % 2 == 0:
		mid = len(lst) // 2
		median = (lst[mid] + lst[mid - 1]) // 2
	else:
		mid = len(lst) // 2
		median = lst[mid]			

	return lst , 'and median is ', median

	
arr = [[1,2,3,4],[3,5,7,8]]

print merge(arr)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(None)
        if len(lists) == 0:
            return None
        
        head.next = lists[0]
        p = ListNode(None)
        q = ListNode(None)
        
        for i in range(1, len(lists)):
            p = head
            q = lists[i]
            
            while q:
                if not p.next:
                    p.next = q
                    break
                if p.next.val < q.val:
                    p = p.next
                else:
                    l = p.next
                    p.next = q
                    q = q.next
                    p.next.next = l
                    p = p.next
        return head.next			