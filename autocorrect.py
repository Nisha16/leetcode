from collections import defaultdict

def generate_autocorrectlist(list_of_words):
	dictionary = {}

	for word in list_of_words:
		for char in range(len(word)):
			prefix = word[:char]
			if prefix not in dictionary:
				temp = set()
				temp.add(word)
				dictionary[prefix] = temp
			if prefix in dictionary:
				dictionary[prefix].add(word)			

	return dictionary
	
def show_autocorrect(stored_words, word):


	auto_correction = generate_autocorrectlist(stored_words)

	print "auto: ", auto_correction
	result = {}

	# last_element = stack()

	for char in range(len(word)):
		pre = word[:char+1]
		#k, v = auto_correction.items()
		if pre in auto_correction.keys():
			#print "char: "+ char
			result[pre] = auto_correction[pre]
			#last_element.push(auto_correction[char])

	return "all words:", result 


a = ['hello', 'hero', 'anil', 'anmol', 'bell']

example = 'herk'

print show_autocorrect(a, example)


			
