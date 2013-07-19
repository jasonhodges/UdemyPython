#!/usr/bin/python

#Polymorphism in Python

class superman:
    def power(self): print("I have super powers")
    def eyes(self): print("I have super vision")
    def brain(self): print("I think during exams")
    def talk(self): print("I speak English and Alien")
    
class human(superman):
    def power(self): print("I have no super powers")
    def eyes(self): print("I have regular vision")
    def brain(self): print("I do not think during exams")
    def talk(self): print("I only speak English")
    
def main():
    jason = human()
    kelley = superman()
    
    for o in (jason, kelley):
        o.power()
        o.eyes()
        o.brain()
        o.talk()
    
    
if __name__ == "__main__": main()
    