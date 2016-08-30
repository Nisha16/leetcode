from collections import defaultdict
import collections
arr = [[11,20],[30,40],[5,10],[40,30], [20,11]]
d= defaultdict(int)
result = []
for k, v in arr:
	d[k] = v

for keys in d:
	if d[keys] in d:

		print 'keys: ', keys

		#if keys == d[keys]:
		result.append([keys, d[keys]])
print d	
k = d.keys()
v = d.values()
print "result: ", result
print "k: ", k
print "v: ", v
# for i in k:
# 	for j in v:
# 		if k[i] == v[j]:
			

