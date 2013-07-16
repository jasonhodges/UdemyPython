#!/usr/bin/python

def main():
    h = open('sample.txt')
    for lines in enumerate(h.readlines()):
        print(lines, end=' ')
    
    
if __name__ == "__main__": main()