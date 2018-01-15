from functools import reduce
def evenlist():
	list1=[]
	for i in range(0,10):
		if i%2==0:
			list1.append(i)
	return list1

def square(x,y):
	return x+y**2
even=evenlist()
print(even)
print(reduce(square,even))
