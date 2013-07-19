#!/usr/bin/python

#Exception in Python 

def main():
    try:
        fh = open("nwfile.txt")
        for lines in fh: print(lines.strip())
    except IOError as e:
        print("typo in file name", e)
if __name__ == "__main__": main()
