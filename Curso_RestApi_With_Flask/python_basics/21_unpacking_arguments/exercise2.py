def add(x, y):
    return x + y

nums = [3, 5]

# efficient way of passing an array as an argument to a fuction 
# this asterik deconstructs, the list so the value 3 goes into x and 5 goes into y. 
print(add(*nums))

# another way of passing values to the arguments:
print(add(x = 10, y = 20))

# efficient way of passing a dictionary as an argument to a function
nums2 = {
    "x": 3,
    "y": 7
}

print(add(**nums2))


