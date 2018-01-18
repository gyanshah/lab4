from random import random
def sort_by_length(*words):
	t=[]
	for word in words:
		t.append((len(word),random(),word))
	t.sort(reverse=True)
	res=[]
	for length,dupsupport,word in t:
		res.append(word)
	return res

print(sort_by_length('Internetworking','Dalhousie','University','Halifax','Nova Scotia','Canada'))
