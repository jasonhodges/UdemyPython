#!/usr/bin/python

#Classes in Python

class human():
    
    def __init__(self):
        print("constructor call")
    
    def brain(self):
        print("i think, but not in exam")
        
    def talk(self):
        print("i speak English")
        
        
def main():
    Jason = human()
    Jason.brain()
    Jason.talk()

    
if __name__ == "__main__": main()