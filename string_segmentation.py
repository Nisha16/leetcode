def can_segment_string_rec(s, dict, solved):
  for i in xrange(1, len(s) + 1):
    first = s[0:i]
    print "first: " , first
    if first in dict:
      second = s[i:]
      print "second: ", second
      if not second:
        return True
        if second in dict:
          return True
        if second not in solved:
          print "solved: ", solved
          if can_segment_string_rec(second, dict, solved):
            return True
          solved.add(second)
  return False

def can_segment_string(s, dict):
  solved = set([])
  return can_segment_string_rec(s, dict, solved)


d = ['hello', 'hell', 'on', 'now']
word = 'hellonow'
print can_segment_string(word,d)    