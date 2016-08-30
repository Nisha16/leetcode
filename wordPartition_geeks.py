def palindrome(word):
	str = word[::-1]
	if str == word:
		print 'palindrome: ', word
		return 'palindrome: ', word
	else:
		print 'not palindrome: ', word
		return 'not palindrome: ', word
		

def partition(phrase):
	for i in range(0,len(phrase)):
		word = phrase[i]
		for j in range(i+1,len(phrase)):
			word = word + phrase[j]
			palindrome(word)

print partition('geeks')			


