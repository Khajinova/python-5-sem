# Первая задача
import numpy as np

class Complex():
    def __init__(self, a =0, b = 0):
        self.a = a
        self.b = b

    def expon(self):
        self.r = np.sqrt(self.a**2 + self.b**2)

        if self.r == 0:
            raise ValueError('Невозможно перевести в экспоненциальную форму')
        
        self.phi = np.arccos(self.a/self.r)
        return self.r, self.phi
    
    def __abs__(self):
        return np.sqrt(self.a**2 + self.b**2)
    
    def __add__(self, other):
        a1 = self.a + other.a
        b1 = self.b + other.b
        return Complex(a1, b1)

    def __sub__(self, other):
        a1 = self.a - other.a
        b1 = self.b - other.b
        return Complex(a1, b1)

    def __mul__(self, other):
        a1 = self.a * other.a - self.b * other.b
        b1 = self.a * other.b + self.b * other.a
        z3 = Complex(a1, b1)
        return z3

    def __truediv__(self, other):
        if ((other.a)**2 + (other.b)**2) != 0:
            a1 = (self.a * other.a + self.b * other.b)/((other.a)**2 + (other.b)**2)
            b1 = (self.a * other.b - self.b * other.a)/((other.a)**2 + (other.b)**2)
            z3 = Complex(a1, b1)
            return z3
        else:
            raise ZeroDivisionError('Деление на 0')
        
    def __radd__(self, other):
        a1 = self.a + other
        b1 = self.b 
        return Complex(a1, b1)

    def __rsub__(self, other):
        a1 = self.a - other
        b1 = self.b 
        return Complex(a1, b1)

    def __mul__(self, other):
        a1 = self.a * other 
        b1 = self.b * other
        z3 = Complex(a1, b1)
        return z3

    def __rtruediv__(self, other):
        if other != 0:
            a1 = self.a / other
            b1 = self.b / other
            z3 = Complex(a1, b1)
            return z3
        else:
            raise ZeroDivisionError('Деление на 0')


    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        else:
            return False

    def __str__(self):
        return "z = " +  str(self.a) + " + i*" + str(self.b)
     
    @property
    def real(self):
        return self.a

    @real.setter
    def real(self, value):
        if type(value) == str:
            raise ValueError("Должно являться числом")
        self.a = value

    @property
    def imag(self):
        return self.b

    @imag.setter
    def imag(self, value):
        if type(value) == str:
            raise ValueError("Должно являться числом")
        self.b = value

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
    

def calculator():
    try:
        print("Введите первое число")
        a1, b1 = map(float, input().split())
        z1 = Complex(a1, b1)

        print("Введите второе число")
        a2, b2 = map(float, input().split())
        z2 = Complex(a2, b2)

        operation = input("Выберите (+, -, *, /): ")

        if operation == "+":
            result = z1 + z2
        elif operation == "-":
            result = z1 - z2
        elif operation == "*":
            result = z1 * z2
        elif operation == "/":
            result = z1 / z2
        else:
            raise ValueError("Некорректная операция")

        print(f"Результат: {result}")
    except ZeroDivisionError:
        print("Деление на ноль")
    except ValueError as e:
        print(e)
