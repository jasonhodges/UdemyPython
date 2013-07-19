#!/usr/bin/python

#Databases in Python

import sqlite3

def main():
    db = sqlite3.connect('test.db')
    db = db.execute('drop table if exists test')
    db= db.execute('create table test(t test, i int)')
    db = db.execute('insert into test(t, i)values(?,?)',('Monday', 1))
    db = db.execute('insert into test(t, i)values(?,?)',('Tuesday', 2))
    db = db.execute('insert into test(t, i)values(?,?)',('Wednesday', 3))
    db = db.execute('insert into test(t, i)values(?,?)',('Thursday', 4))
    db = db.execute('insert into test(t, i)values(?,?)',('Friday', 5))
    
    s = db.execute('select * from test order by i')
    for row in s:
        print(row)
        
    
if __name__=="__main__": main()