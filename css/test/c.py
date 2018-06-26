import os

testwalk=os.walk('D:\\request')
for a, b,c in testwalk:
	print (a)
	print(b)
	print(c)
	print('-----------------------')