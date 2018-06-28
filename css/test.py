import csv
from configparser import ConfigParser
import os
import csv

# pa=os.listdir(os.getcwd())
# for x in pa:

# 	path1=os.path.splitext(x)
# 	if path1:
# 		print(x)
# 		print(os.getcwd())

#当前目录以及子目录下所有'.py'的文件

# walk=os.walk('.')

# for dirn, subdir,file in walk:

# 	for filename in file:

# 		if  os.path.splitext(filename)[1]=='.py':
# 			print (filename)

# 			print(os.path.abspath(dirn))
# 			print('******************')

# import json
# d=dict(name='bob',age='20',score='85')

# class cdc(object):
# 	"""docstring for cdc"""
# 	def __init__(self, name,age):
# 		self.name = name
# 		self.age=age

# def cdc2dict(std):
# 	return {'name':std.name,'age':std.age}

# s=cdc('嘻嘻',20)
# print(json.dumps(s,default=cdc2dict,ensure_ascii=False))
# 			

# with open("../data/homepage.csv") as csvfile:
#     arglists = csv.DictReader(csvfile)
#     for args in arglists:
#         print(args.get)



import re

color='rgba(1, 1, 1, 1)'
co=re.findall(r"\d+",color)
print(co)
