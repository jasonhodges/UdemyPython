#!/usr/bin/python

#Format Method in String in Python
print ('Hello World')

x, y = 1, 2
print (x, y)

print 'this is {} and that is {}'.format(x, y)

s = 'this is {} and that is {}'
print id(s)

news = s.format(x, y)
print id(news)

print 'this is {} and that is {}'.format(y, x)

print 'this is {1} and that is {0} another is {1} and one more {0}'.format(x, y)