def operate(operator, *args):
    result = 0
    if operator == '+':
        for i in args:
            result += i
    elif operator == '-':
        for i in args:
            result -= i 
    elif operator == '*':
        result = 1
        for i in args:
            result *= i
    elif operator == '/':
        result = 1
        for i in args:
            result /= i

    return result