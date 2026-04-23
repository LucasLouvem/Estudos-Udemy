#Dicionarios em python
dicionario = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}
print(dicionario)

print(dicionario["marca"])

print(dicionario["modelo"])

print(dicionario["ano"])

print(dicionario.keys())

dicionario["cor"] = "vermelho"
print(dicionario)

print(dicionario.get("modelo"))

print(dicionario.keys())

print(dicionario.values())

print(dicionario.items())

# Atualizar Dicionario

dicionario["ano"] = 2020
print(dicionario)
dicionario.update({"ano": 2021})
print(dicionario)

# adicionar um novo item
dicionario["preco"] = 30000
print(dicionario)
dicionario.update({"Fipe": 35000})
print(dicionario)

# Remover um item
dicionario.pop("cor")
print(dicionario)
del dicionario["preco"]
print(dicionario)
clear_dicionario = dicionario.clear()
print(clear_dicionario, "\n")

# Looping em dicionarios
dicionario = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}
for chave in dicionario:
    print(chave)

for x in dicionario:
    print(f"Valor: {dicionario[x]}")

for x in dicionario.keys():
    print(f"Chave: {x}")

for x in dicionario.values():
    print(f"Valor: {x}")

for x, y in dicionario.items():
    print(f"Chave: {x}, Valor: {y}")

# Copiar um dicionario
dicionario_copia = dicionario.copy()
print(dicionario_copia)

dicionario_copia["ano"] = 2020
print(f"dicionario_copia: {dicionario_copia}")
print(f"dicionario: {dicionario}")

dicionario_copia2 = dict(dicionario)
print(f"dicionario_copia2 com dict: {dicionario_copia2}")