def serialize_word(S):
	result = ''
	for word in S:
		result += word
		result += ' '

	return result

input = ['Anil', 'hey', 'enjoyy.']

def deserailize_word(sentence):
	sub_string = ''
	output = []
	for char in sentence:
		if char != ' ':
			sub_string += char
			#print "sub: " + sub_string
		else:
			output.append(sub_string)
			sub_string = ''
			#print 'out: ', output
	#output.append(sub_string)
	return output	
				

print serialize_word(input)	

sentence = 'Python string slicing syntax as well as links to primary documentation.'
print deserailize_word(sentence)	
