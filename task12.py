word=dict()
fin=open("words.txt")
def dictionary(c):
	for char in fin:
		word[char]=char
	if c in word:
		return True

print(dictionary('gnome'))
