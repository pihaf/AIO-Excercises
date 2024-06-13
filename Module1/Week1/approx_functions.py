positive_int_check = "n must be a positive integer"

# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def approx_sin(x, n):
    if n <= 0:
        print(positive_int_check)
        return None
    
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    
    return result

def approx_cos(x, n):
    if n <= 0:
        print(positive_int_check)
        return None
    
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    
    return result

def approx_sinh(x, n):
    if n <= 0:
        print(positive_int_check)
        return None
    
    result = 0
    for i in range(n):
        result += (x ** (2 * i + 1)) / factorial(2 * i + 1)
    
    return result

def approx_cosh(x, n):
    if n <= 0:
        print(positive_int_check)
        return None
    
    result = 0
    for i in range(n):
        result += (x ** (2 * i)) / factorial(2 * i)
    
    return result