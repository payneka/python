#!/usr/bin/env python

def close (num1, num2, num3):
    import math
    if math.fabs(num1-num2)<num3:
        return True
    else:
        return False

if __name__ == '__main__':

    num1 = 1
    num2 = 4
    num3 = 4

    print close(num1,num2,num3)
    
