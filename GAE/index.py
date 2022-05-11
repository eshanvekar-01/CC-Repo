print 'Hello World';

n1=0
n2=1

for i in range(8):
	str = "{} "
	print(str.format(n1))
	n3 = n1+n2
	n1 = n2
	n2 = n3