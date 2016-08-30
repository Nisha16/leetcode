def shortestPalindrome(s):
	s_rev = s[::-1]
	string = s + '&' + s_rev
	print "string: " + string
	prefix = [0 for i in range(len(string))]
	for j in range(1, len(string)):
		i = prefix[j - 1]
		if i > 0 and string[j] != string[i]:
			i = prefix[i - 1]
		prefix[j] = i + (string[j] == string[i])
		print "string[j]: ", string[j]
		print "string[i]: ", string[i]
		print "prefix: " ,prefix
	return s_rev[:len(s)-prefix[-1]]+s


def longestPalindrome(s):
    l = len(s)
    if l <= 2:
        if (s[0] != s[l-1]): return ''
        else: return s
        
    result = ''
    for i in range(0,l):
        palindrome = SearchPalindrome(s, i, i)
        if len(palindrome) > len(result): 
            result = palindrome
            print "R: " + result
        palindrome = SearchPalindrome(s, i, i+1)
        if len(palindrome) > len(result): 
            result = palindrome
            print "R1: " + result
    return result
                    
def SearchPalindrome(string, start, end):
    while(start>=0 and end < len(string) and string[start]==string[end]):
        start -= 1
        end += 1
    print "string: " + string[start+1:end]  
    return string[start+1:end]			

#print shortestPalindrome('abc')

print longestPalindrome('forgeeksskeegfor')					
