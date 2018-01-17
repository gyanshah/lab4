f = open('words.txt')

def create_word_dict(c):
	word_dict = dict()
	for line in f:
		word = line.strip()
		word_dict[word] = word
	if c in word_dict:
		return True
	else:
		return False

print(create_word_dict("gyan"))
