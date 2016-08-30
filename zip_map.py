d = [raw_input().split() for i in xrange(input())]
print 'first i: ' , i
e = dict(zip([i[0] for i in d], [sum(map(float,i[1:]))/(len(i)-1) for i in d]))
print e
print "%.2f" % e[raw_input()]
