def Is_palindrome(s):
	start = 0
	end = len(s) - 1
	while start <= len(s)//2 and end >= len(s) // 2:
		if s[start] == s[end]:
			pass
		else:
			return False
		start += 1
		end -= 1	
	return True
	
print Is_palindrome('sore was I ere I saw eros')			
				
