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

s = dict((x,"Even") if x%2 ==0 else (x,"Odd") for x in range(18))
print(s)

# dict1={"one":1,"two":2,"three":3}
# duplicate=[]
# for a in range(len(dict1)):
#
#     sml=[a for a in dict1.values() if a ==min(dict1.values())]
#     key1=[k for k,v in dict1.items() if v ==min(dict1.values())]
#     del dict1(key1)
#     duplicate.append(sml)

#print(sml)

ce = "vishnu is gooooog boy in nature"
from collections import Counter
print((Counter(ce)))
#print(key1)
