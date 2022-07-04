#
#
#
#
#
# # dict1={"one":1,"two":2,"three":3}
# # duplicate=[]
# # for a in range(len(dict1)):
# #
# #     sml=[a for a in dict1.values() if a ==min(dict1.values())]
# #     key1=[k for k,v in dict1.items() if v ==min(dict1.values())]
# #     del dict1(key1)
# #     duplicate.append(sml)
#
# #print(sml)
#
# # ce = "vishnu is gooooog boy in nature"
# # from collections import Counter
# # print((Counter(ce)))
# # #print(key1)
#
#
# #
# #import pyqrcode
# # from pyqrcode import QRCode
# #
# # s = "vishnu is good boy "
# #
# # code = pyqrcode.create(s)
# #
# # code.svg("mypng.svg",scale =1)'
#
#
# import random
#
# # n = random.randint(1,100)
# #
# #
# # guess = int(input("please enter a possible numer fomr 1 to 100"))
# #
# # while guess != n:
# #
# # 	if guess < n:
# # 		print("your entered value is too low")
# # 		guess =  int (input ("please renter your value again.."))
# # 	elif guess > n:
# # 		print("Value you entered is too high , please enter below number")
# # 		guess = int(input("please renter your value again.."))
# # 	elif guess ==n:
# # 		break
# # print("congrats you have entered a perfect value..")\
# #1. Find all of the numbers from 1–1000 that are divisible by 8
#
# # a= [ i for i in range(1,1000) if i%8==0]
# #
# # print(a)
#
# #7. Use a nested list comprehension to find all of the numbers from 1–1000
# # that are divisible by any single digit besides 1 (2–9)
#
# dic = [ f for f in range(2,100) if  True in [True for divisor in range(99,999) if f%divisor==0] ]
#
# print((dic))
#
# mat = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
#
# a =[ c for a in mat for c in a if c%2==0]
#
# print(a)
#
# mylist = [9, 3, 6, 1, 6, 0, 8, 2, 4, 7]
# list_b = [6, 4, 6, 1, 2, 2]
# v={i : mylist.index(i) for i in list_b}
#
# print(v)
#
# stop = [ 7 , 8 ,9]
#
# basha = [ w  for w in range(1,20) if w not in stop]
#
# print(basha)
#
# sentences = ["a new world record was set",
#              "in the holy city of ayodhya",
#              "on the eve of diwali on tuesday",
#              "with over three lakh diya or earthen lamps",
#              "lit up simultaneously on the banks of the sarayu river"]
#
# stopwords = ['for',  'of', 'the', 'and', 'to', 'in', 'on', 'with']
#
# good_words=[ actualWord  for word in sentences for actualWord in word.split(",") if actualWord not in stopwords]
#
# print("".join(good_words))
#
# negate = [a for a  in range(3,8) ]
#
# solutio = [ -a if a  in range(3,8) else a for a in range(1,20)]
#
# print(solutio)
#
# dict_1 = {"1":"abc","2":"def","3":"ghi"}
# dict_2 = {"3":"abc","4":"def"}
#
# #
# # for k in  (dic1):
# #     #print("a :",k,v[1])
# #     # print(dic2.keys())
# #     # print(a
# #     if k not  in dic2:
# #         print("dc1 :",dic1[k])
# #         print("dc2 :",dic2[k])
# #         dic1[k] = dic2[k]
# #     else:
# #         #value = dic2[k]
# #         dic1[k] = "value"
# for key, value in dict_2.items():
#     if key in dict_1:
#         # if isinstance(dict_1[key], list):
#         #     dict_1[key].append(value)
#         # else:
#
#             dict_1[key]+=value
#     else:
#         dict_1[key] = value
# print(dict_1)
# import sys
# print(sys.maxint)
#
#
#
#
#
#

# maxinta= [9,2,3,4,1,2,3,4]
# x=0
# for s in a:
#     x=x^s
#     #print(x)
# print(x)
#
# import numpy as np
# frid =  np.arange(1,10,0.5).reshape((2,9))
#
# print(frid)

s =  "absvnns22wv111sdfsj333"

d = "".join([ "@" if i =="2"
      else "$" if i=="1"
      else "#" if i=="3"
      else i


    for i in s
])

print(d)