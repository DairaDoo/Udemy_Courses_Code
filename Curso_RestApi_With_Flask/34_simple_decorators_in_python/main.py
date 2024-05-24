def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function():
        if user["access level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user["username"]}"
        
    return secure_function

get_admin_password = make_secure(get_admin_password) # aquí se reasigna el valor de la función get_admin_password por el retornado en make_secure.
user = {"username": "jose", "access level": "admin"}
print(get_admin_password())
