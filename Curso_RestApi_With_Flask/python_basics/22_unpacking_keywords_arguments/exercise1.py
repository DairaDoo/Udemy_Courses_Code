def named(**kwargs):
    """This function collect names arguments into a dictionary"""
    print(kwargs)
    
# you can pass it this way 
named(name = "Bob", age = 25)

# also you can pass it this way too
details = {
    "name": "Dairan",
    "age": 21,
}

# we use the both asteriks to deconstruct the dictionary
named(**details)


# new function exercise

def print_nicely(**kwargs):
    named(**kwargs)
    
    for arg, value in kwargs.items(): # I can here use items because kwargs in a dictionary.
        print(f"{arg}: {value}")

print_nicely(name = "Jose", age = 28)