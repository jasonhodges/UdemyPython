#!/usr/bin/python

def main():
    x, y = 0, 1
    while y < 100:
        print(y, end= ' ')
        x, y = y , x+y
    
if __name__ == "__main__": main()