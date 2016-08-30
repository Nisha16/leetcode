from collections import defaultdict

def minimum(s,t):
    expected = defaultdict(int)
    current = defaultdict(int)
    start = 0
    i = 0
    min_start = 0
    min_len = 0
    count = 0
    # print s
    # print t
    # print '\n'

    for char in t:
        expected[char] += 1

    print expected

    for char in s:
        # print "i = ", i
        # print "char = ", char
        if char in expected:
            current[char] += 1
            # print "current", current

            if current[char] <= expected[char]:
                count += 1
                # print "count = ", count

        if count == len(t):
            # print "count == len(t)"
            # print "start = ", start
            # print "min_len = ", min_len
            while s[start] not in expected or current[s[start]] > expected[s[start]]:
                # print "s[" + str(start) + "] = " + s[start]
                if s[start] in current:
                    current[s[start]] -= 1
                start += 1
                # print "start = ", start
                # print "current = ", current

            # print i - start + 1
            # print min_len
            if min_len > i - start + 1 or min_len == 0:
                min_len = i - start + 1
                # print "min_len > i = ", start, "new_min_len = ", min_len
                min_start = start

        i += 1

    if min_len <= 0:
        return ''

    return s[min_start:min_start+min_len]

print minimum('ADOBECODEBANC','ABC')







