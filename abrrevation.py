#Given a list of words and an abbreviation, I have to write a function which returns true or 
#false about whether the abbreviation maps to exactly one word or not

def abbrevation(list_of_words,word):
	dictionary = {}
	for words in list_of_words:
		abbr = words[0] + str(len(words) - 2) + words[-1]
		try:
			dictionary[abbr].add(words)
		except:
			dictionary[abbr] = set()
			dictionary[abbr].add(words)
	print dictionary
	print "length: ", len(dictionary['c2e'])		

	word_abbr = word[0] + str(len(word) - 2) + word[-1]
	for keys in dictionary:
		if keys == word_abbr:
			if word in dictionary[keys] or len(dictionary[keys]) > 1:
				return False
			else:
				return True
	#print "dictionary: ", dictionary			
	return True			

	# return dictionary
	

list_of_words = ['deer','door','cake','card']

print abbrevation(list_of_words, 'cake')

# def Is_abbrevation_unique(word):
# 	word_abbr = word[0] + str(len(word) - 2) + word[-1]
# 	for items in dictionary:
# 		if key == word_abbr:
# 			if word in dictionary[key] and len(dictionary[key] == 1:
# 				return True
# 			else:
# 				return False
# 	return True					

				
