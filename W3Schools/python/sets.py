# Juntando Sets

# Union e Update
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Union
set3 = set1.union(set2)
print(set3)  # Output: {1, 2, 3, 4, 5}
set3 = set1 | set2
print(set3)  # Output: {1, 2, 3, 4, 5}
# Update
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}

# Juntando varios sets

setA = {1, 2}
setB = {"b", "c"}
setC = {True, False}
setD = {1.5, 2.5}

myset = setA.union(setB, setC, setD)
print(myset)  # Output: {1, 2, 'b', 'c', True, False, 1.5, 2.5}

# Juntando sets com tuplas e listas
setX = {1, 2}
tupleY = (3, 4)
listZ = [5, 6]

z = setX.union(tupleY, listZ) # -> Também pode ser escrito como: z = setX | set(tupleY) | set(listZ)
print(z)  # Output: {1, 2, 3, 4, 5, 6}

# O operador | so permite juntar conjuntos com conjuntos, esse metodo a seguir da errado
# setX = {1, 2}
# tupleY = (3, 4)
# z = setX | tupleY  # Isso vai gerar um erro, pois o operador

# devera ser feito da maneira abaixo, convertendo a tupla e a lista para sets antes de usar o operador |
setX = {1, 2}
tupleY = ("a", "b")
listZ = [False, True]
z = setX | set(tupleY) | set(listZ) # -> convertendo a tupla e a lista para sets antes de usar o operador | 
print(z)  # Output: {1, 2, 'a', 'b', False, True}
