def histogram(c):
	val=dict()
	for i in c:
		val[i]=(val.get(i,0))+1
	return val

"""def invert_dict(d):
	inverse=dict()
	for key in d:
		val=d[key]
		if val not in inverse:
			inverse[val]=[key]
		else:
			inverse[val].append(key)
	return inverse"""
def invert_dict(dic):
	inverse = {}
	for key, val in dic.items():
		inverse.setdefault(val, []).append(key)
	return inverse

h=histogram("Internetworking")
inverse=invert_dict(h)
print(inverse)
