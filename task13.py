def histogram(c):
	val=dict()
	for i in c:
		val[i]=(val.get(i,0))+1
	return val

h=histogram('Internetworking')
print (h)
