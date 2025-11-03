import math
def add(a:float,b:float)-> float: # def add(a,b)
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return  ("Sıfıra bölme hatası")
    return a/b

def mod(a,b):
    if b==0:
        return  ("Sıfıra bölme hatası")
    return a%b

def pow_op(a,b):
    return a**b

def sqrt(a:float)->float:
    if (a<0):
        return ValueError("negatif olmaz")
    
    return math.sqrt(a)