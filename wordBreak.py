
def wordBreak(sentence, dictionary):
	if sentence in dictionary:
		return sentence
	length = len(sentence)
	#prefix  = ''
	for i in range(1,length):
		prefix = sentence[0:i]
		if prefix in dictionary:
			suffix = sentence[i:length]
			segSuffix = wordBreak(suffix, dictionary)
			if segSuffix != None:
				#print prefix + ' ' + segSuffix
				return True	
	return False			


	

list_of_words = {'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango'}

sentence = 'ilovesamsung'

print wordBreak1(sentence,list_of_words)

			
