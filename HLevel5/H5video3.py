#!/usr/bin/python

#Join and SPlit a String in Python

print 'this is a string'

s = 'this is a string'

print s.split()

print 'this is a string'.split()

new = s.split()
for i in new: print(i)

print ' '.join(new)

print ':'.join(new)