def histogram(c):
	val=dict()
	for i in c:
		val[i]=(val.get(i,0))+1
	return val

def reverse_lookup(d,v):
	similar_number_of_keys=[]
	for k in d:
		if d[k] == v:
			similar_number_of_keys.append(k)
	return similar_number_of_keys
h=histogram('Internetworking')
k=reverse_lookup(h,1)
print(k)
