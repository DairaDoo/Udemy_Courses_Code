def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
        
    return total
    
print("Result:", multiply(1, 3, 5))


# this functions first receives as many arguments as you want.
# but then you have to pass a named argument for the operator.
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(apply(1, 2, 1, 1, operator = "*"))
        
