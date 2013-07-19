#!/usr/bin/python

#Raising Exception in Python 

def main():
    try:
        fh = open("newfile.txt")
        if 'newfile.pdf'.endswith('.txt'):
            for lines in fh: print(lines.strip())
        else: raise ValueError("wrong file extension")
    except IOError as e:
        print("typo in file name", e)
if __name__ == "__main__": main()