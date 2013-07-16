#!/usr/bin/python

def main():
    var = 22.0
    print(type(var), var)
    
    var = 22 / 9
    print(type(var), var)
    
    var = 22 // 9
    print(type(var), var)
    
    var = round(22 / 9, 3)
    print(type(var), var)
    
    var = 22 % 9
    print(type(var), var)
    
    var = int(22.0)
    print(type(var), var)
    
    var = float(22)
    print(type(var), var)
    
if __name__ == "__main__": main()