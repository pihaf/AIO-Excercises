# Question 5
def check_the_number(number) :
    list_of_numbers = []
    result = ""
    for i in range (1, 5) :
        list_of_numbers.append(i)

    if number in list_of_numbers :
        result = "True"
    if number not in list_of_numbers :
        result = "False"
    return result

N = 2
results = check_the_number(N)
#print(results)

# Question 6
def append_min_max( data , max , min) :
    result = []
    for i in data :
        if i < min:
            result.append(min)
        elif i > max :
            result.append(max)
        else :
            result.append(i)
    return result

my_list = [10, 2, 5, 0, 1]
max_val = 2
min_val = 1
# print(append_min_max(data = my_list, max_val = max_val, min_val = min_val))

# Question 7
def extend_list(x, y):
    # Your code here
    #Su dung extend de noi y vao x
    x.extend(y)
    return x

list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]

#print(extend_list(list_num1, extend_list(list_num2, list_num3)))

# Question 8
def find_min_in_list(n):
    return min(n)

my_list = [1, 2, 3, -1]
#print(find_min_in_list(my_list))

# Question 9
def find_max_in_list(n):
    # Your code here
    return max(n)

my_list = [1, 9, 9, 0]
#print(find_max_in_list(my_list))

# Question 10
def check_equal_num(integers, number=1):
    return any(x == number for x in integers)

my_list = [1, 2, 3, 4]
#print(check_equal_num(my_list, 2))

# Question 11
def find_mean(list_nums = [0, 1, 2]):
    var = 0
    for i in list_nums :
        var += i
    return var / len(list_nums)

#print(find_mean())

# Question 12
def check_if_divisible_by_three(data):
    var = []
    for i in data:
        # Neu i chia het cho 3 thi them i vao list var
        if i % 3 == 0:
            var.append(i)
    return var

#print(check_if_divisible_by_three([1, 2, 3, 5, 6]))

# Question 13
def factorial(y):
    var = 1
    while y > 1:
        var *= y
        y -= 1
    return var

#print(factorial(4))

# Question 14
def reverse_string(x):
    x = list(x)
    x = x[::-1]
    reversed_string = ''.join(x)
    return reversed_string

x = 'apricot'
#print(reverse_string(x))

# Question 15
def check_positive_num(x):
    # Neu x >0 tra ve 'T', nguoc lai tra ve 'N'
    if x > 0:
        return 'T'
    else:
        return 'N'

def my_function(data):
    res = [check_positive_num(x) for x in data]
    return res

data = [2, 3, 5, -1]
#print(my_function(data))

# Question 16
def function_helper(x, data):
    for i in data:
        # Neu x == i thi return 0
        if x == i:
            return 0
    return 1

def find_unique_num(data):
    res = []
    for i in data:
        if function_helper(i, res):
            res.append(i)
    return res

lst = [9, 9, 8, 1, 1]
#print(find_unique_num(lst))
