def both(*args, **kwargs):
    """
    This functions receives a series of arguments
    converting them into a tuple and a series of
    named arguments converting them into a dictionary
    """
    print(args)
    print(kwargs)
   
# we can also print them both using args and kwargs 
both(1, 2, 3, name = "Bob", age = 25)


# real example using this:
# def post(url, data = None, json = None, **kwargs):
#     return request('post', url, data = data, json = json, **kwargs)


def myfunction(**kwargs):
    print(kwargs)
    
# you must pass a dictionary to it. 
myfunction(**"Bob") # Error, must be mapping
myfunction(**None)  # Error