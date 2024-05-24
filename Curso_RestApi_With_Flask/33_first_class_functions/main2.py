# importamos itemgetter
from operator import itemgetter # forma más avanzada de hacerlo. 

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
        raise RuntimeError(f"Could not find an element with {expected}")
    
friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

def get_friend_name(friend):
    return friend["name"]

# first way of doing it using get_friend_name
print(search(friends, "Rolf Smith", get_friend_name))

# we can do this too using a lambda. 

print(search(friends, "Rolf Smith", lambda friend: friend["name"]))

# this is a more advanced way of doing it.
print(search(friends, "Rolf Smith", itemgetter("name"))) 