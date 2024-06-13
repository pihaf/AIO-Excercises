import math

# Function to check if number
def is_number(n):
    try :
        float(n) # Type - casting the string to 'float'.
                 # If string is not a valid 'float', it ’ll raise 'ValueError' exception
    except ValueError :
        return False
    return True

def sigmoid(x):
    return 1 / (1 + math.e**(-x))

def relu(x):
    return max(0, x)

def elu(x, alpha = 0.01):
    return x if x >= 0 else alpha * (math.e**x - 1)

def calculate_activation_functions():
    # Get user input and validate the input if number
    x = input("Input x = ")
    if not is_number(x):
        print("x must be a number")
        return
    else:
        x = float(x)

    # Get user input function and validate name
    activation_function = input("Input activation function (sigmoid|relu|elu): ")
    if activation_function not in ("sigmoid", "relu", "elu"):
        print(f'{activation_function} is not supported')
        return

    # Calculate required function
    if activation_function.strip() == "sigmoid":
        result = sigmoid(x)
    elif activation_function.strip() == "relu":
        result = elu(x)
    elif activation_function.strip() == "elu":
        result = relu(x)
    
    print(f'{activation_function}: f({x}) = {result}')
