# aquí ambos tienen id iguales, en python si algo puede cambiar significa que es mutable.

a = []
b = []

print("-----------------------")

print(id(a))
print(id(b))

# aquí el id es el mismo en memoria ya que la lista a y b, tiene el mismo valor

a = []
b = a
print("-----------------------")

print(id(a))
print(id(b))

# con los numeros, aunque sean creados en distintas variables
# en python se utilza la misma ubicación en memoria (mismo id)

a = 8920
b = 8920

print("-----------------------")

print(id(a))
print(id(b))

# en python la mayoría de las cosas son mutables, excepto tuples, string, booleans, y algunas más.