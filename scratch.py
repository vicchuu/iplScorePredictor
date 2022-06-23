a = [[1,2,3], [3,4,5],[5,6,7]]
d=[]

[d.append(j) for i in a  for j in i if j not in d ]
print(d)

dic =  {
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}


print(sorted(dic.items() , key =  lambda x :x[0] , reverse=False ))