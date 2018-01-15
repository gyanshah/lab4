from functools import reduce
my_list=[1,2,3,4]
my_list.append([5,6,7,8])
my_list[4].append([9,10,11,12])
my_list[4][4].append([13,14,15,16])
print (my_list)	
def nested_sum(my_list):	
	sum1=0
	sum2=0
	sum3=0
	for i in my_list:
		if (type(i)==int):
			sum1=sum1+i
		else:
			for j in i:
				if type(j)==int:
					sum2 += j
				else:
					sum3=sum3+sum(j)
	return sum1+sum2+sum3

print(nested_sum(my_list))
