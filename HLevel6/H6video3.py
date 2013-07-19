#!/usr/bin/python

#Dictionary in Python

d = {'one':1, 'two':2, 'three':3}
print d 
print type(d)

e = dict(four=4, five=5, six=6)
print e

for i in d:print(i)

for i, j in d.items():print (i, j)

g = dict(ten=10, el=11, tw=12, **d)
print g 

print d.get('one')