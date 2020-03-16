#Benchmark Functions
'''
References:






'''
from math import pi

#Rastrigin function
#min f(0,...,0) = 0
def Rastrigin(n,x):
    a = 10
    
    obj = a*n+sum(a*cos(2*pi))
    return obj

#Ackley function
#min f(0,...,0) = 0
def Ackley():
    a = 20
    b = 0.2
    c = 2*pi
    obj = 
    return obj

#Beale function
#min f(3,0.5) = 0   
def Beale(x, y):
    a = sqrt(1.5 - x + x*y)    
    b = sqrt(2.25 - x - x*(y**2))
    c = sqrt(2.625 - x + x*(y**3))
    obj = a + b + c
    return obj

