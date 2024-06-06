"""
blocklist.py

This file just contains the blocklist of the JWT tokens. It will be imported by 
app and the logout resource so that tokens can be added to the blocklist when the
user logs out.

"""

# normalmente es mejor usar una base de datos que el set de python.
# ya que al reiniciar el app, el blocklist fue borrado, los python
# sets no se quedan luego de dar un restar al app.
# una buena forma es usando Redis de python.
# AL TERMINAR EL CURSO IMPLEMENTAR REDIS AQUÍ.
BLOCKLIST = set()