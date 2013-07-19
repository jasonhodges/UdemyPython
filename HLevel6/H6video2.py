#!/usr/bin/python

#More about List and Tuple in Python

t = tuple(range(20))
print t
 
print type(t)

l = list(range(20))
print l

print t[5]

print 100 in l 

print 100 not in l 

print l.count(5)

print l.append(100)

print l 

l.extend(range(10))

print l 

 