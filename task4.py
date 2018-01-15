my_list=list(range(0,10))
def multiple(n):
	list1=[]
	for i in my_list:	
		if n%5==0:
			list1.append(i)
	return list1

print(list(filter(multiple,my_list)))
