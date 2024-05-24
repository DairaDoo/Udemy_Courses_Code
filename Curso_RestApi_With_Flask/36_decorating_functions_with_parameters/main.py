import functools
user = {"username": "jose", "access level": "admin"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user["username"]}"
        
    return secure_function

@make_secure
def get_admin_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"
    

# get_admin_password = make_secure(get_admin_password) < el make_secure ahorra esta linea de código

print(get_admin_password("billing"))
print(get_admin_password.__name__) # si no usamos el function.wraps, el nombre de get_admin_password cambiara a secure_function.
