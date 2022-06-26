




# dict1={"one":1,"two":2,"three":3}
# duplicate=[]
# for a in range(len(dict1)):
#
#     sml=[a for a in dict1.values() if a ==min(dict1.values())]
#     key1=[k for k,v in dict1.items() if v ==min(dict1.values())]
#     del dict1(key1)
#     duplicate.append(sml)

#print(sml)

# ce = "vishnu is gooooog boy in nature"
# from collections import Counter
# print((Counter(ce)))
# #print(key1)


#
#import pyqrcode
# from pyqrcode import QRCode
#
# s = "vishnu is good boy "
#
# code = pyqrcode.create(s)
#
# code.svg("mypng.svg",scale =1)'


import random

# n = random.randint(1,100)
#
#
# guess = int(input("please enter a possible numer fomr 1 to 100"))
#
# while guess != n:
#
# 	if guess < n:
# 		print("your entered value is too low")
# 		guess =  int (input ("please renter your value again.."))
# 	elif guess > n:
# 		print("Value you entered is too high , please enter below number")
# 		guess = int(input("please renter your value again.."))
# 	elif guess ==n:
# 		break
# print("congrats you have entered a perfect value..")\
#1. Find all of the numbers from 1–1000 that are divisible by 8

# a= [ i for i in range(1,1000) if i%8==0]
#
# print(a)

#7. Use a nested list comprehension to find all of the numbers from 1–1000
# that are divisible by any single digit besides 1 (2–9)

dic = [ f for f in range(2,100) if  True in [True for divisor in range(2,10) if f%divisor==0] ]

print(len(dic))
