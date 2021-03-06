'''
1.  Identify base case
2. Identify stop case
3. Return values of function
'''

# Factorial Looping

def factorial_loop(value):
    sum = 1
    if(value > 0):
        for i in range(1,value+1):
            sum = sum * i
    print(sum)

factorial_loop(5)

# Factorial Recursion

def factorial_recursion(value):
    if(value == 0):
        return 1
    elif(value > 1):
        return value * factorial_recursion(value-1)
    else:
        return 1

print(factorial_recursion(5))

# Fibonacchi loop f(x) = f(x - 1) + f(x - 2)

def fib_loop(value):
    case = [0,1]
    if(value >= 2):
        for i in range(2,value + 1):
            case.append(case[i-1] + case[i-2])
    return case[value]

print(fib_loop(100))


def fib_recursion(value):
    if(value < 2):
        return value
    else:
        return fib_recursion(value - 1) + fib_recursion(value - 2)

print(fib_recursion(10))

#Anything that can be implemented reecursively ,  can be immplemented with loops

# Reverse a string with recursion


def reverse_string_recursion(value : str) -> str:
    if(value == ""):
        return ""
    else:
        return reverse_string_recursion(value[1:]) + value[0]

print(reverse_string_recursion("Hello"))


def reverse_string_loop(value : str) -> str:
    stub = ""
    i = len(value) - 1
    while(i >= 0):
        stub = stub + value[i]
        i = i -1
    return stub

print(reverse_string_loop("Hello"))
