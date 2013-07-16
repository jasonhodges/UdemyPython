#!/usr/bin/python


def main():
    var = (1, 2, 3, 4, 5)
    print(type(var), var)
    
def main():
    var = [1, 2, 3, 4, 5]
    var.append(8)
    var.insert(0, 9)
    print(type(var), var)
    
def main():
    d = {'one':1, 'two':2, 'three':3}
    print(type(d), d)
    
    for k in d:
        print (k, d[k])
        
def main():
    d = dict(
             one=1, two=2, three='stringvalue'
    )
    print(type(d), d)
    
    for k in d:
        print (k, d[k])
        
def main():
    s = 'string'
    print(type(s), s)
    
    
if __name__ == "__main__": main()