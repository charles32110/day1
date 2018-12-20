#bool_learning



def booltest(n,m):
    x = bool(n > m)
    return x
print booltest(3,4)
print booltest(4,3)


#use import
import math
#get the function
print dir(math)
#    >>['__doc__', '__file__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
#get specific way to use  console >> help(math.sqrt)
def cal(a):
    b = math.sqrt(a)
    return b
print cal(16)

#if statement

def flight(a):
#define the flight time at 12:00 as 12
    b = 12
    if b >= a:
        return('early')
    else:
        return('delay')
print flight(16)