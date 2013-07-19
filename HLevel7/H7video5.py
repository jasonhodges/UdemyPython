#!/usr/bin/python

#Inheritance in Python

class superman:
    def power(self): print("I have super powers")
    def talk(self): print("I speak all languages")
    
class human(superman):
    
    def __init__(self):
        print("constructor call")
    
    def brain(self):
        print("i think, but not in exam")
        
    def talk(self):
        super().talk()
        print("i speak English")
        
        
def main():
    Jason = human()
    Jason.brain()
    Jason.power()
    Jason.talk()
    Jason.talk()
    

    
if __name__ == "__main__": main()