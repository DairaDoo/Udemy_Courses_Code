def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator = divide) # pasamos la funcion divide como argumento a la variable operator. 
print(result)