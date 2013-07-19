#!/usr/bin/python

#Intro to Functions in Python

def main():
    igneus(12, 1, 2, 3, 4, 5, 6, 7)
    
def igneus(num, num1=1, num2=2, *args):
    print("www.igneustech.com", num, num1, num2, args)
    for i in args:
        print(i)
        
if __name__ == "__main__": main()