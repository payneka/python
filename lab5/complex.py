#!/usr/bin/env python

import numpy as np

class Complex(object):
    def __init__(self, re=0, im=0):
        self.re,self.im = float(re),float(im)

    def __str__(self):
        if self.im <0:
            sign = ''
        else:
            sign = '+'
        return'(%g%s%gi)' %(self.re, sign, self.im)
        
    def __add__(self, other):
        try:
            return Complex(self.re+other.re, self.im+other.re)
        except:
            return Complex(self.re+other, self.im)
        
    def __radd__(self, other):
        try:
            return Complex(self.re+other.re, self.im+other.re)
        except:
            return Complex(self.re+other, self.im)
        
    def __sub__(self,other):
        try:
            return Complex(self.re-other.re, self.im-other.re)
        except:
            return Complex(self.re-other, self.im)
        
    def __rsub__(self,other):
        try:
            return Complex(self.re-other.re, self.im-other.re)
        except:
            return Complex(self.re-other, self.im)

    def __mul__(self,other):
        try:
            return Complex(self.re*other.re - self.im*other.im, self.im*other.re + self.re*other.im)
        except:
            return Complex(self.re*other, self.im)
        
    def __rmul__(self,other):
        try:
            return Complex(self.re*other.re - self.im*other.im, self.im*other.re + self.re*other.im)
        except:
            return Complex(self.re*other, self.im)

    def __div__(self,other):
       
        try:
            top = self * (~other)
            bottom = other * (~other)
            return Complex(top.re/bottom.re, top.im/bottom.re)
        except:
            return self / Complex(other)

    def __rdiv__(self,other):
        return Complex(other)/self   

    def __invert__(self):
        return Complex(self.re,-self.im)
    
    __repr__=__str__


#Function tests
#basic
##a = Complex(1.0,2.3)
##b = Complex(2)
##c = Complex()
##
##print a
##print b
##print c
##
###string
##a = Complex(1,2)
##b = Complex(1,-2)
##print a
##print b

###addition
##a = Complex(1, 2)
##b = Complex(3, 4)
##print 'Addition'
##print a + b
##print a + 1
##print 1 + a
##
###Subtraction
##a = Complex(1, 2)
##b = Complex(3, 3)
##print 'Subtraction'
##print a - b
##print a - 1
##print 1 - a
##
###Multiply
##a = Complex(1, 2)
##b = Complex(3, 4)
##print 'Multiply'
##print a * b
##print a * 1
##print 1 * a
##
###Divide
##a = Complex(1, 2)
##b = Complex(3, 4)
##print 'Divide'
##print a / b
##print a / 1
##print 1 / a
##print -1/a
##
###Conjugate
##a = Complex(1,2)
##print 'Complex Conjugate'
##print ~a

