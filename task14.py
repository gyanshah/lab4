def histogram(c):
	val=dict()
	for i in c:
		val[i]=(val.get(i,0))+1
	return val

def print_hist(string):
	k_list=sorted(string.keys())
	for key in k_list:
		print(key,string.get(key))

h=histogram('Gyan Shah')
print_hist(h)
