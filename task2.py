from functools import reduce
def evenlist():
	list1=[]
	for i in range(100,500):
		if i%2==0:
			list1.append(i)
	return list1

def summation(x,y):
	return x+y

even=evenlist()
print(reduce(summation,even))
