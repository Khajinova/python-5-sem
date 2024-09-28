import numpy as np

class Complex():
    def __init__(self, a =0, b = 0):
        self.a = a
        self.b = b
    
    def expon(self):
        self.r = np.sqrt(self.a**2 + self.b**2)
        self.phi = np.arccos(self.a/self.r)
        return self.r, self.phi

def summo(z1: Complex, z2: Complex):
    a1 = z1.a + z2.a
    b1 = z1.b + z2.b
    z3 = Complex(a1, b1)
    return z3

def razn(z1: Complex, z2: Complex):
    a1 = z1.a - z2.a
    b1 = z1.b - z2.b
    z3 = Complex(a1, b1)
    return z3

def umno(z1: Complex, z2: Complex):
    a1 = z1.a * z2.a - z1.b * z2.b
    b1 = z1.a * z2.b + z1.b * z2.a
    z3 = Complex(a1, b1)
    return z3


def dlet(z1: Complex, z2: Complex):
    if ((z2.a)**2 + (z2.b)**2) != 0:
        a1 = (z1.a * z2.a + z1.b * z2.b)/((z2.a)**2 + (z2.b)**2)
        b1 = (z1.a * z2.b - z1.b * z2.a)/((z2.a)**2 + (z2.b)**2)
        z3 = Complex(a1, b1)
        return z3
    else: 
        print('error')
        return
