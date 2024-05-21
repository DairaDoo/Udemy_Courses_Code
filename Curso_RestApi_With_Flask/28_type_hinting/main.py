from typing import List # Tuple, Set, etc...

# (variable: tipo de dato a recibir como argumento) -> resultado esperado
def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)