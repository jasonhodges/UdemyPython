#!/usr/bin/python

def main():
    x, y = 1, 2
    if x<y:
        print('this is True condition')
    else:
        print('this is not True')
    
if __name__ == "__main__": main()

def main2():
    day = 'Monday'
    if day == 'Monday':
        print('Its not my fav')
    elif day == 'Tuesday':
        print('Not fav either')
    elif day == 'Saturday':
        print('Party time!')
    else:
        print('The others days')
    
if __name__ == "__main__": main2()